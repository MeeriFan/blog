#from datetime import datetime
#from datetime import date
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
		if self.username == '' or\
			self.email == '' or\
			self.first_name == '' or\
			self.last_name == '' or\
			self.password == '':
			message = 'You have to fill out all fields.'
			return False, message
		"""
		for attribute, value in self.__dict__.items():
			for key, user_input in value.items():
				if user_input == '':
					message = 'You have to fill out all fields.'
					return False, message
		"""
		if not len(self.password) >= 8:
			message = 'Your password needs to be at least 8 characters long.'
			return False, message
		if not any(c.isalpha() for c in self.password):
			message = 'Your password should at least contain one alphabetic character.'
			return False, message
		if not self.password == repeated_pw:
			message = 'The password and repeated password have to be the same.'
			return False, message
		if not '@' in self.email and not '.' in self.email:
			message = 'Your email address is not valid.'
			return False, message
		return True, None

	def is_already_in_db(self):
		return User.select().where(User.email == self.email).exists()

	def generate_salt(self):
		self.salt = uuid4().hex
		self.save()

	def hash_password(self):
		return hashlib.sha256(self.salt.encode()+self.password.encode()).hexdigest()

	def login_valid(self):
		db_user = self.get_user_by_mail()
		self.salt = db_user.salt
		self.password = self.hash_password()
		return User.select().where(
			User.email == self.email, 
			User.password == self.password
		).exists()

	def get_user_by_mail(self):
		return User.get(User.email == self.email)

	def get_user_by_id(self):
		return User.get(User.id == self.id)
