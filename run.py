from bottle import template, Bottle, debug, run, request, response
from bottle import redirect, static_file
from uuid import uuid4
from blog_classes import User

app = Bottle()


def set_app_cookie(user_id):
	key = uuid4().hex
	response.set_cookie('session_id', key, secret=SECRET)
	session_dict[key] = user_id


def delete_app_cookie(deactivate_user=False):
	session_key = get_key()
	if deactivate_user:
		User.deactivate_user(session_dict[session_key])
	del session_dict[session_key]
	response.delete_cookie('session_id', secret=SECRET)


def get_key():
	return request.get_cookie('session_id', secret=SECRET)


def user_logged_in():
	if get_key():
		return 'yes'
	return 'no'


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
	if session_key not in session_dict:
		info = {
			'message': 'You must be logged in.',
			'logged_in': 'no',
			'href': 'index'
		}
		return template('error.tpl', info)
	else:
		user = User.get_user(session_dict[session_key])
		message = 'Welcome back, ' + user.first_name + ' ' + user.last_name + '!'
		info = {
			'message': message,
			'logged_in': 'yes'
		}
		return template('profile.tpl', info)


@app.route('/users')
def list_users():
	list_users = User.get_all()
	info = {
		'title': 'List of all Users',
		'logged_in': user_logged_in(),
		'users': list_users
	}
	return template('users.tpl', info)


@app.route('/users/<user_id:int>')
def specific_user(user_id):
	user = User.get_user(user_id)
	info = {
		'user': user,
		'title': 'Profile of %s' % user.username,
		'logged_in': user_logged_in()
	}
	return template('single_user.tpl', info)


@app.route('/login')
def login_form():
	info = {
		'title': 'Login',
		'message': 'Please log in.',
		'logged_in': 'no'
	}
	return template('login.tpl', info)


@app.route('/login/failed')
def login_form_failed():
	info = {
		'title': 'Login',
		'message': 'Login failed. Please try again.',
		'logged_in': 'no'
	}
	return template('login.tpl', info)


@app.route('/login/inactive')
def account_inactive():
	info = {
		'title': 'Login',
		'message': 'Your account is inactive. Please reactivate.',
		'logged_in': 'no',
		'link': 'Reactivate my account'
	}
	return template('login.tpl', info)


@app.post('/login')
@app.post('/login/failed')
@app.post('/login/inactive')
def do_login():
	user = User(
		email=request.forms.get('email'),
		password=request.forms.get('pw')
	)
	if user.verify_login():
		user = User.by_email(user.email)
		set_app_cookie(user.id)
		message = 'Welcome back, ' + user.username + '!'
		info = {
			'message': message,
			'logged_in': 'yes'
		}
		return template('profile.tpl', info)
	else:
		return redirect('/login/failed')


@app.post('/logout')
def do_logout():
	delete_app_cookie()
	return redirect('/index')


@app.route('/registration')
def registration(message='Please fill out the form completely for \
	registration.', user=User(), repeated_pw=''):
	info = {
		'title': 'Registration',
		'message': message,
		'logged_in': 'no',
		'u_f_name': user.first_name,
		'u_l_name': user.last_name,
		'u_name': user.username,
		'u_email': user.email,
		'u_pw': user.password,
		'u_pw_r': repeated_pw
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
			set_app_cookie(new_user.id)
			info = {
				'f_name': new_user.first_name,
				'l_name': new_user.last_name,
				'logged_in': 'yes',
				'message': 'Thank you for registrating to this microblog!'
			}
			return template('thank_you.tpl', info)
		else:
			return registration(message=error, u=new_user, r_pw=repeated_passwpord)
	else:
		info = {
			'message': 'You are already registered.',
			'href': 'registration',
			'logged_in': 'no'
		}
		return template('error.tpl', info)


@app.route('/deactivate')
def deactivate_user():
	info = {
		'title': 'Good Bye?',
		'message': 'You really want to deactivate you profile? This means you have to \
		register again to reactivate your profile. All your data will be kept.',
		'logged_in': 'yes'
	}
	return template('deactivate.tpl', info)


@app.post('/deactivate')
def do_deactivate():
	delete_app_cookie(deactivate_user=True)
	info = {
		'logged_in': 'no',
		'specification': 'deactivated'
	}
	return template('sorry.tpl', info)


@app.route('/delete')
def delete_account():
	info = {
		'title': 'Good Bye?',
		'message': 'You really want to delete your account? This means that your \
		whole profile will be deleted and there is no way back. Are you sure? \
		You should consider to deactivate your profile',
		'logged_in': 'yes'
	}
	return template('delete.tpl', info)


@app.post('/delete')
def do_delete():
	User.delete_user(session_dict[get_key()])
	delete_app_cookie()
	info = {
		'logged_in': 'no',
		'specification': 'deleted'
	}
	return template('sorry.tpl', info)


@app.route('/static/<path:path>')
def static_files(path):
	return static_file(path, 'static/')

if __name__ == '__main__':
	debug(True)
	run(app, host='localhost', port=8080, reloader=True)