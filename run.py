
from bottle import template, Bottle, debug, run, request,response, redirect

app = Bottle()

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


@app.route('/profile')
def profile():
	# das hier geht nur, wenn man eingeloggt ist!
	username = request.get_cookie('logged_in_as', False)
	if not username:
		return 'You must be logged in!'
	else:
		return 'Welcome back, ' + username

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
	admin = {
		'admin_mail' : 'admin@google.net',
		'password' : 'adminpassword'
	}
	email = request.forms.get('email')
	pw = request.forms.get('pw')
	if email == admin['admin_mail'] and pw == admin['password']:
		response.set_cookie('user_authorised', 'True')
		message = 'Welcome back!'
		return template('registration.tpl', message=message)
	else:
		return redirect('/login/failed')

	return redirect('/login/admin')

	# hint: perform validation if login is correct
	# hint: response.set_cookie

if __name__ == '__main__':
	debug(True)
	run(app, host='localhost', port=8080, reloader=True)