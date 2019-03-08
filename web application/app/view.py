from app import app
from flask import render_template
from movie_parser import MoviesList

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/pogoda')
def pogoda():
	return render_template('pogoda.html')

@app.route('/curs')
def curs():
	return render_template('curs.html')

@app.route('/films')
def films():
	return render_template('films.html')

@app.route('/zadanie')
def zadanie():
	return render_template('zadanie.html')

