
from bottle import template, Bottle, debug, run

app = Bottle()

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def greet(name='Stranger'):
	#return template('Hello {{t_name}}, how are you?', t_name=name)
	info = {'t_name' : name, 'title' : 'Welcome'}
	return template('welcome_template.tpl', info)


if __name__ == '__main__':
	debug(True)
	run(app, host='localhost', port=8080, reloader=True)