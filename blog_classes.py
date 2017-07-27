import hashlib
from uuid import uuid4
from peewee import SqliteDatabase, Model
from peewee import CharField, TextField, ForeignKeyField
from peewee import DateTimeField
from markdown import markdown
import datetime
import re

db = SqliteDatabase('blog.db')


class BaseModel(Model):
    class Meta:
        database = db


class Postable(BaseModel):
    FORMAT_DATE = "%a, %d. %b %Y, %H:%M:%S"

    def nice_date(self):
        return self.created_at.strftime(self.FORMAT_DATE)

    def render_body(self):
        return markdown(self.body, output_format='html5')


class User(BaseModel):
    username = CharField(default='')
    email = CharField(default='')
    first_name = CharField(default='')
    last_name = CharField(default='')
    password = CharField(default='')
    salt = CharField()
    profile_text = TextField(default='')

    class Meta:
        db_table = 'users'

    def is_valid(self, repeated_pw):
        if '' in [self.username, self.email, self.first_name,
                  self.last_name, self.password]:
            return False, 'You have to fill out all fields.'
        if not len(self.password) >= 8:
            return False, 'Your password needs to be \
                        at least 8 characters long.'
        if not any(c.isalpha() for c in self.password):
            return False, 'Your password should at least contain \
                                        one alphabetic character.'
        if not self.password == repeated_pw:
            return False, 'The password and repeated password \
                                        have to be the same.'
        if '@' not in self.email:
            return False, 'Your email address is not valid.'
        if User.select().where(User.username == self.username):
            return False, 'This username is already taken. Please \
                                            use a different one.'
        if not re.match("^[A-Za-z0-9_-.~]*$", self.username):
            return False, 'For your username please use only: \
                                        a-z, A-Z, 0-9, ., ~, _ or -.'
        return True, None

    def is_already_in_db(self):
        return User.select().where(User.email == self.email).exists()

    def generate_salt(self):
        self.salt = uuid4().hex
        self.save()

    def hash_password(self):
        return hashlib.sha256(
            self.salt.encode() + self.password.encode()
            ).hexdigest()

    def verify_login(self):
        if self.email != '':
            db_user = User.by_email(self.email)
        elif self.username != '':
            db_user = User.by_username(self.username)
        if not db_user:
            return False
        self.salt = db_user.salt
        self.password = self.hash_password()
        return User.select().where(
            (User.email == self.email) | (User.username == self.username),
            User.password == self.password
        ).exists()

    def by_email(mail):
        try:
            return User.get(User.email == mail)
        except:
            return None

    def by_id(user_id):
        try:
            return User.get(User.id == user_id)
        except:
            return None

    def by_username(username):
        try:
            return User.get(User.username == username)
        except:
            return None

    def delete_user(username):
        user = User.by_username(username)
        user.delete_instance()

    def deactivate_user(username):
        user = User.by_username(username)
        user.active = False
        user.save()

    def get_all():
        return User.select()

    def save_profile_text(self, profile_text):
        self.profile_text = profile_text
        self.save()

    def path(self):
        return '/users/%s' % self.slug()

    def posts_path(self):
        return '/users/%s/posts' % self.slug()

    def index_path():
        return '/users'

    def slug(self):
        return self.username


class Post(Postable):
    user = ForeignKeyField(User, related_name='posts')
    title = CharField(default='')
    body = TextField(default='')
    created_at = DateTimeField()

    class Meta:
        db_table = 'posts'

    def get_abstract(self):
        return markdown(self.body[:50], output_format='html5')

    def get_post(post_id):
        try:
            return Post.get(Post.id == post_id)
        except:
            return None

    def matching_posts(searchword):
        return Post.select().where(
            Post.body.contains(searchword) | Post.title.contains(searchword)
        )

    def path(self):
        return '/users/%s/posts/%d' % (self.user.slug(), self.id)


class Comment(Postable):
    body = TextField(default='')
    user = ForeignKeyField(User, related_name='comments')
    post = ForeignKeyField(Post, related_name='comments')
    created_at = DateTimeField()

    class Meta:
        db_table = 'comments'
