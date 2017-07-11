from datetime import datetime
from datetime import date

class User(object):
	"""

	"""

	all_posts = []

	def __init__(self, email, first_name, last_name):
		self.email = str(email)
		self.first_name = str(first_name)
		self.last_name = str(last_name)
		self.posts = self.posts()

	def full_name(self):
		return self.first_name + ' ' + self.last_name

	def posts(self):
		for single_post in Post.list_of_posts:
			if self == single_post.author:
				self.all_posts.append(single_post)
		return self.all_posts

class Post(object):
	"""

	"""
	list_of_posts = []

	def __init__(self, title, body, User, year=0, month=0, day=0):
		self.title = str(title)
		self.body = str(body)
		try:
			self.publish_date = date(year, month, day)
		except ValueError:
			self.publish_date = ''
		self.created_at = datetime.now()
		self.author = User
		Post.list_of_posts.append(self)

	def is_published(self):
		return self.publish_date != ''


class Comment(object):
	"""

	"""

	def __init__(self, body, User, Post):
		self.author_email = User.email
		self.body = str(body)
		self.created_at = datetime.now()
		self.post = Post