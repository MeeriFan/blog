
from bottle import template, Bottle, debug, run

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


if __name__ == '__main__':
	debug(True)
	run(app, host='localhost', port=8080, reloader=True)