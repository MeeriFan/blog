import peewee
from bottle import template, Bottle, debug, run, request,response, redirect
from uuid import uuid4
from blog_classes import User

app = Bottle()

def get_user_by_mail(u_email, u_pw):
	try:
		return User.get(User.email == u_email, User.password == u_pw)
	except:
		return None

def get_user(user_id):
	return User.get(User.id == user_id)

def register_validation(user_register):
	for key in user_register:
		if user_register[key] == '':
			message = 'You have to fill out all fields.'
			return False, message
	if not len(user_register['u_pw']) >= 8:
		message = 'The password needs to be at least 8 signs long.'
		return False, message
	if not any(c.isalpha() for c in user_register['u_pw']):
		message = 'Your password should at least contain one alphabetic character.'
		return False, message
	if not user_register['u_pw'] == user_register['u_pw_r']:
		message = 'The password and repeated password have to be the same.'
		return False, message
	if not '@' in user_register['u_email'] and not '.' in user_register['u_email']:
		message = 'Your email address is not valid.'
		return False, message
	return True, ''

@app.route('/')
@app.route('/index')
def index():
	session_key = request.get_cookie('session_id', secret=SECRET)
	if session_key in session_dict:
		return template('index.tpl', logged_in='yes')
	else:
		return template('index.tpl', logged_in='no')

session_dict = {}

SECRET = 'dogcatmouse'

@app.route('/profile')
def profile():
	# das hier geht nur, wenn man eingeloggt ist!
	session_key = request.get_cookie('session_id', secret=SECRET)
	if not session_key in session_dict:
		info = {
			'message' : 'You must be logged in.',
			'logged_in' : 'no',
			'href' : 'index'
		}
		return template('error.tpl', info)
	else:
		user = get_user(session_dict[session_key])
		message = 'Welcome back, ' + user.first_name +' '+ user.last_name + '!'
		info = {
			'message' : message,
			'logged_in' : 'yes'
		}
		return template('profile.tpl', info)

@app.route('/login')
def login_form():
	info = {
		'title' : 'Login',
		'message' : 'Please log in.',
		'logged_in' : 'no'
	}
	return template('login.tpl', info)

@app.route('/login/failed')
def login_form_failed():
	info = {
		'title' : 'Login',
		'message' : 'Login failed. Please try again.',
		'logged_in' : 'no'
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
		response.set_cookie('session_id', key, secret=SECRET)
		session_dict[key] = user.id
		message = 'Welcome back, ' + user.username + '!'
		info = {
			'message' : message,
			'logged_in' : 'yes'
		}
		return template('profile.tpl', info)
	else:
		return redirect('/login/failed')

@app.route('/logout')
def logout():
	return template('logout.tpl', logged_in='yes')

@app.post('/logout')
def do_logout():
	session_key = request.get_cookie('session_id', secret=SECRET)
	del session_dict[session_key]
	response.delete_cookie('session_id', secret=SECRET)
	return redirect('/index')

@app.route('/registration')
def registration(message='Please fill out the form completely for registration.',user_info={'u_f_name':'','u_l_name':'','u_name':'','u_email':'','u_pw':'','u_pw_r':''}):
	info = {
		'title' : 'Registration',
		'message' : message,
		'logged_in' : 'no',
		'u_f_name' : user_info['u_f_name'],
		'u_l_name' : user_info['u_l_name'],
		'u_name' : user_info['u_name'],
		'u_email' : user_info['u_email'],
		'u_pw' : user_info['u_pw'],
		'u_pw_r' : user_info['u_pw_r']
	}
	return template('registration.tpl', info)

@app.post('/registration')
def do_registration():
	user_info =	{
		'u_f_name' : request.forms.get('first_name'),
		'u_l_name' : request.forms.get('last_name'),
		'u_name' : request.forms.get('nickname'),
		'u_email' : request.forms.get('email'),
		'u_pw' : request.forms.get('pw'),
		'u_pw_r' : request.forms.get('r_pw')
	}
	input_validated, message = register_validation(user_info)
	if not input_validated:
		return registration(message=message, user_info=user_info)
	user_known = get_user_by_mail(user_info['u_email'], user_info['u_pw'])
	if not user_known:
		new_user = User(
			username=user_info['u_name'], 
			email=user_info['u_email'], 
			first_name=user_info['u_f_name'],
			last_name=user_info['u_l_name'],
			password=user_info['u_pw']
		)
		new_user.save()
		key = uuid4().hex
		response.set_cookie('session_id', key, secret=SECRET)
		session_dict[key] = new_user.id
		info = {
			'f_name' : user_info['u_f_name'],
			'l_name' : user_info['u_l_name'],
			'logged_in' : 'yes'
		}
		return template('thank_you.tpl', info)
	else:
		info = {
			'message' : 'You are already registered.',
			'href' : 'registration',
			'logged_in' : 'no'
		}
		return template('error.tpl', info)

@app.route('/delete')
def delete_user():
	info = {
		'title' : 'Good Bye?',
		'message' : 'You really want to delete you profile?',
		'logged_in' : 'yes'
	}
	return template('delete.tpl', info)

@app.post('/delete')
def do_delete():
	session_key = request.get_cookie('session_id', secret=SECRET)
	user_id = session_dict[session_key]
	old_user = get_user(user_id)
	old_user.delete_instance()
	del session_dict[session_key]
	response.delete_cookie('session_id', secret=SECRET)
	return template('sorry.tpl', logged_in='no')


if __name__ == '__main__':
	debug(True)
	run(app, host='localhost', port=8080, reloader=True)