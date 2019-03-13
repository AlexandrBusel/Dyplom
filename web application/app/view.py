from app import app
from flask import render_template
from movie_parser import MoviesList

import requests

import lxml
from lxml import html

@app.route('/')
def index():
	return render_template('index.html')

# @app.route('/pogoda')
# def pogoda():

# 	city_name = "в Минске"
# 	city_id = 625144
# 	appid = "812e89737fcf7992cc92812abee5c137"
	
# 	res = requests.get("http://api.openweathermap.org/data/2.5/weather",
# 	    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
# 	data = res.json()
# 	return data
	# return ("Сегодня:", city_name),	("состояние погоды:", data['weather'][0]['description']), ("Температура воздуха:", data['main']['temp']), ("Температура min:", data['main']['temp_min']), ("Температура max:", data['main']['temp_max'])
	# return render_template('pogoda.html')

# @app.route('/curs')
# def curs():
# 	return render_template('curs.html')

# @app.route('/curs', methods=["POST"])
# def curs_post():
		
# 	usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
			
# 	response = requests.get(usd).json()
		
# 	name = response['Cur_Name']
# 	price = response['Cur_OfficialRate']
	
# 	return str(name), str(price)

	# return render_template('curs.html')

# @app.route('/films')
# def films():
	
	
# 	# return 'Hello world'
# 	return render_template('films.html')


@app.route('/zadanie')
def zadanie():
	return render_template('zadanie.html')

