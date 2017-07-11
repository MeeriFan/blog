from datetime import datetime

class User(object):
	"""

	"""

	posts = []

	def __init__(self, email, first_name, last_name, posts):
		self.email = str(email)
		self.first_name = str(first_name)
		self.last_name = str(last_name)
		self.posts = self.posts()

	def full_name(self):
		return self.first_name + ' ' + self.last_name

	def posts(self):
		for single_post in Post:
			if self == Post.author:
				self.posts.append(single_post)
		return self.posts

class Post(User):
	"""

	"""

	def __init__(self, title, body, publish_date=None):
		self.title = str(title)
		self.body = str(body)
		self.publish_date = datetime(publish_date)
		self.created_at = datetime.now()
		self.author = User

		def is_published(self):
			return publish_date != None

class Comment(Post):
	"""

	"""

	def __init__(self, author_email='', body=''):
		self.author_email = str(author_email)
		self.body = str(body)
		self.created_at = datetime.now()
		self.post = Post