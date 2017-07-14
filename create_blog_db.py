import peewee
from blog_db import Users
from blog_db import db

def create_tables():
	db.create_tables(
		[Users],
		safe=True)

if __name__ == '__main__':
	print('Creating tables...')
	db.connect()
	create_tables()
	db.close()