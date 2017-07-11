from datetime import datetime

class User(object):
	"""

	"""

	posts = []

	def __init__(self, email='', first_name='', last_name='', posts):
		self.email = str(email)
		self.first_name = str(first_name)
		self.last_name = last_name
		self.posts = posts

	def full_name(self):
		return self.first_name + ' ' + self.last_name

	def posts(self):
		pass

class Post(object):
	"""

	"""

	def __init__(self, title='', body='' , publish_date=None):
		self.title = str(title)
		self.body = str(body)
		self.publish_date = datetime(publish_date)
		self.created_at = datetime.now()
		self.author = ''

		def is_published(self):
			return publish_date != None

class Comment(object):
	"""

	"""

	def __init__(self, author_email='', body='', post):
		self.author_email = author_email
		self.body = body
		self.created_at = datetime.now()
		self.post = posts