from bottle import template, Bottle, debug, run, request,response, redirect, static_file
from uuid import uuid4
from blog_classes import User

app = Bottle()

def setting_cookie(user_id):
	key = uuid4().hex
	response.set_cookie('session_id', key, secret=SECRET)
	session_dict[key] = user_id

def deleting_cookie(delete_user=False):
	session_key = get_key()
	if delete_user:
		User.delete_user(session_dict[session_key])
	del session_dict[session_key]
	response.delete_cookie('session_id', secret=SECRET)

def get_key():	
	return request.get_cookie('session_id', secret=SECRET)

@app.route('/')
@app.route('/index')
def index():
	session_key = get_key()
	if session_key in session_dict:
		return template('index.tpl', logged_in='yes')
	else:
		return template('index.tpl', logged_in='no')

session_dict = {}

SECRET = 'dogcatmouse'

@app.route('/profile')
def profile():
	session_key = get_key()
	if not session_key in session_dict:
		info = {
			'message' : 'You must be logged in.',
			'logged_in' : 'no',
			'href' : 'index'
		}
		return template('error.tpl', info)
	else:
		user = User.get_user(session_dict[session_key])
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
	user = User(
		email=request.forms.get('email'),
		password=request.forms.get('pw')
	)
	if user.verify_login():
		user = user.get_db_user_by_mail()
		setting_cookie(user.id)
		message = 'Welcome back, ' + user.username + '!'
		info = {
			'message' : message,
			'logged_in' : 'yes'
		}
		return template('profile.tpl', info)
	else:
		return redirect('/login/failed')

@app.post('/logout')
def do_logout():
	deleting_cookie()
	return redirect('/index')

@app.route('/registration')
def registration(message='Please fill out the form completely for registration.',user=User(), r_pw=''):
	info = {
		'title' : 'Registration',
		'message' : message,
		'logged_in' : 'no',
		'u_f_name' : user.first_name,
		'u_l_name' : user.last_name,
		'u_name' : user.username,
		'u_email' : user.email,
		'u_pw' : user.password,
		'u_pw_r' : r_pw
	}
	return template('registration.tpl', info)

@app.post('/registration')
def do_registration():
	new_user = User(
		username=request.forms.get('nickname'),
		email=request.forms.get('email'),
		first_name=request.forms.get('first_name'),
		last_name=request.forms.get('last_name'),
		password=request.forms.get('pw')
	)
	if not new_user.is_already_in_db():
		repeated_passwpord = request.forms.get('r_pw')
		valid, error = new_user.is_valid(repeated_passwpord)
		if valid:
			new_user.generate_salt()
			new_user.password = new_user.hash_password()
			new_user.save()
			setting_cookie(new_user.id)
			info = {
				'f_name' : new_user.first_name,
				'l_name' : new_user.last_name,
				'logged_in' : 'yes'
			}
			return template('thank_you.tpl', info)
		else:
			return registration(message=error, u=new_user, r_pw=repeated_passwpord) 
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
	deleting_cookie(delete_user=True)
	return template('sorry.tpl', logged_in='no')

@app.route('/static/<path:path>')
def static_files(path):
    return static_file(path, 'static/')

if __name__ == '__main__':
	debug(True)
	run(app, host='localhost', port=8080, reloader=True)