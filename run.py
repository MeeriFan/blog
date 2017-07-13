from app import app
from bottle import run
from bottle import debug

debug(True)
run(app, host='localhost', port=8080)