import peewee
from blog_classes import User, Post
from blog_classes import db


def delete_tables():
    db.drop_tables(
        [User, Post],
        safe=True)

if __name__ == '__main__':
    print('Dropping tables...')
    db.connect()
    delete_tables()
    db.close()
