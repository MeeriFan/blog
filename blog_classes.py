import hashlib
from uuid import uuid4
from peewee import SqliteDatabase, Model
from peewee import CharField

db = SqliteDatabase('blog.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(default='')
    email = CharField(default='')
    first_name = CharField(default='')
    last_name = CharField(default='')
    password = CharField(default='')
    salt = CharField()

    class Meta:
        db_table = 'users'

    def is_valid(self, repeated_pw):
        if '' in [self.username, self.email, self.first_name,
                  self.last_name, self.password]:
            return False, 'You have to fill out all fields.'
        if not len(self.password) >= 8:
            return False, 'Your password needs to be at least 8 characters long.'
        if not any(c.isalpha() for c in self.password):
            return False, 'Your password should at least contain one alphabetic character.'
        if not self.password == repeated_pw:
            return False, 'The password and repeated password have to be the same.'
        if '@' not in self.email and '.' not in self.email:
            return False, 'Your email address is not valid.'
        return True, None

    def is_already_in_db(self):
        return User.select().where(User.email == self.email).exists()

    def generate_salt(self):
        self.salt = uuid4().hex
        self.save()

    def hash_password(self):
        return hashlib.sha256(self.salt.encode() + self.password.encode()).hexdigest()

    def verify_login(self):
        db_user = User.by_email(self.email)
        if not db_user:
            return False
        self.salt = db_user.salt
        self.password = self.hash_password()
        return User.select().where(
            User.email == self.email,
            User.password == self.password
        ).exists()

    def by_email(mail):
        try:
            return User.get(User.email == mail)
        except:
            return None

    def get_user(user_id):
        try:
            return User.get(User.id == user_id)
        except:
            return None

    def delete_user(user_id):
        user = User.get_user(user_id)
        user.delete_instance()

    def deactivate_user(user_id):
        user = User.get_user(user_id)
        user.active = False
        user.save()

    def get_all():
        return User.select()
