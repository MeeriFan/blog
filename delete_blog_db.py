import peewee
from blog_db import Users
from blog_db import db 

def delete_tables():
	db.drop_tables(
		[Users],
		safe=True)

if __name__ == '__main__':
	print('Dropping tables...')
	db.connect()
	delete_tables()
	db.close()