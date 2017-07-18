from datetime import datetime
from datetime import date
from peewee import SqliteDatabase, Model
from peewee import CharField

db = SqliteDatabase('blog.db')

class BaseModel(Model):
	class Meta:
		database = db

class User(BaseModel):
	username = CharField()
	email = CharField()
	first_name = CharField()
	last_name = CharField()
	password = CharField()
	salt = CharField()

	class Meta:
		db_table = 'users'

	def has_email(self):
		return self.email != None