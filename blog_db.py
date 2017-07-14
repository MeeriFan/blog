from peewee import SqliteDatabase, Model
from peewee import CharField

db = SqliteDatabase('blog.db')

class BaseModel(Model):
	class Meta:
		database = db

class Users(BaseModel):
	username = CharField()
	email = CharField()
	first_name = CharField()
	last_name = CharField()
	password = CharField()