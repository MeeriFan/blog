import peewee
import sys
from blog_classes import User, Post, Comment
from blog_classes import db


def create_tables():
    db.create_tables(
        [User, Post, Comment],
        safe=True)

if __name__ == '__main__':
    sys.stderr.write('Creating tables...')
    db.connect()
    create_tables()
    db.close()
