from datetime import datetime
from datetime import date

class User(object):
	"""
	Returns User object

	Attribute:
		* email of the user
		* fist_name of user
		* last_name of user

	Methods:
		* full_name -> returns full name of user
		* posts -> returns list of posts the user was author of
	"""

	def __init__(self, email, first_name, last_name):
		self.email = email
		self.first_name = first_name
		self.last_name = last_name

	def full_name(self):
		return self.first_name + ' ' + self.last_name

	def posts(self):
		all_posts = []
		for single_post in Post.list_of_posts:
			if self == single_post.author:
				all_posts.append(single_post)
		return all_posts

	def __repr__(self):
		return self.full_name()

class Post(object):
	"""
	Returns Post object

	Static attribute:
		* list of all posts

	Attribute:
		* title of post
		* body of post -> content of post
		* publish_date 
		* created_at (datetime)
		* author -> user who wrote post

	Methods:
		* is_published -> returns bool 
		* save -> to save all posts in static attribute
	"""
	list_of_posts = []

	def __init__(self, title, body, user, year=0, month=0, day=0):
		self.title = title
		self.body = body
		try:
			self.publish_date = date(year, month, day)
		except ValueError:
			self.publish_date = ''
		self.created_at = datetime.now()
		self.author = user
		self.save()

	def is_published(self):
		return self.publish_date != '' and self.publish_date <= date.today()

	def save(self):
		Post.list_of_posts.append(self) # TODO: duplikate vermeiden


class Comment(object):
	"""
	Returns Comment object

	Attribute:
		* email address of user
		* body -> content of comment
		* created_at
		* post which was commented
	"""

	def __init__(self, body, user, post):
		self.author_email = user.email
		self.body = body
		self.created_at = datetime.now()
		self.post = post