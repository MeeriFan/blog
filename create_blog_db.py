import peewee
from blog_classes import User
from blog_classes import db

def create_tables():
	db.create_tables(
		[User],
		safe=True)

if __name__ == '__main__':
	print('Creating tables...')
	db.connect()
	create_tables()
	db.close()