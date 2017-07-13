from app import app
from bottle import template

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def greet(name='Stranger'):
	#return template('Hello {{t_name}}, how are you?', t_name=name)
	return template('welcome_template.tpl', t_name=name)