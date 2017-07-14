import peewee
from bottle import template, Bottle, debug, run, request,response, redirect
from uuid import uuid4
from blog_classes import User

app = Bottle()

def get_user_by_mail(u_email, u_pw):
	try:
		user = User.get(User.email == u_email, User.password == u_pw)
	except:
		user = None
	return user

def get_user(user_id):
	return User.get(User.id == user_id)

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def greet(name='Stranger'):
	info = {
		't_name' : name, 
		'title' : 'Welcome',
		'posts' : [
			{
				'author' : 'John',
				'body' : 'Beautiful day in Portland!'
			},
			{
				'author' : 'Susan',
				'body' : 'The Avengers movie was so cool!' 
			},
			{
				'author' : 'Tobias',
				'body' : 'My new Trainee is the best!'
			}
		]
	}
	return template('index.tpl', info)

session_dict = {}

SECRET = 'dogcatmouse'

@app.route('/profile')
def profile():
	# das hier geht nur, wenn man eingeloggt ist!
	session_key = request.get_cookie('session_id', secret=SECRET)
	if not session_key in session_dict:
		return 'You must be logged in!'
	else:
		user = get_user(session_dict[session_key])
		return 'Welcome back, ' + user.first_name + ' ' + user.last_name + '!'

@app.route('/login')
def login_form():
	info = {
		'title' : 'Login',
		'message' : 'Please log in.'
	}
	return template('login.tpl', info)

@app.route('/login/failed')
def login_form_failed():
	info = {
		'title' : 'Login',
		'message' : 'Login failed. Please try again.'
	}
	return template('login.tpl', info)

@app.post('/login')
@app.post('/login/failed')
def do_login():
	email = request.forms.get('email')
	pw = request.forms.get('pw')
	user = get_user_by_mail(email, pw)
	if user:
		key = uuid4().hex
		response.set_cookie('session_id', key, secret=SECRET ,max_age=40)
		session_dict[key] = user.id
		message = 'Welcome back, ' + user.username + '!'
		return template('registration.tpl', message=message)
	else:
		return redirect('/login/failed')

if __name__ == '__main__':
	debug(True)
	run(app, host='localhost', port=8080, reloader=True)