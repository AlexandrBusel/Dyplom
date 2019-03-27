
from app import app
from flask import render_template
from movies import MoviesList
from curses import curses
from pogoda import weather

import requests


@app.route('/')
def index():
	return render_template('index.html', movies = MoviesList().create_movies_list(), curs = curses())
	pass

@app.route('/pogoda')
def pogoda():
	return render_template('pogoda.html', pogoda = weather())
	pass

@app.route('/zadanie')
def zadanie():
	return render_template('zadanie.html')

