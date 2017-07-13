from app import app
from bottle import template

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def greet(name='Stranger'):
	#return template('Hello {{t_name}}, how are you?', t_name=name)
	info = {'t_name' : name, 'title' : 'Welcome'}
	return template('welcome_template.tpl', info)