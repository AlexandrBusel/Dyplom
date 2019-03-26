

import requests

from flask import Blueprint
from flask import render_template
from flask import request

from lxml import html



afisha = Blueprint('afisha', __name__, template_folder='templates')
cursy = Blueprint('cursy', __name__, template_folder='templates')

@afisha.route('/')


def index():
    datefilm = request.args.get('datefilm')

    if datefilm != None:
        movies_params = {
        'url':'https://afisha.tut.by/film/{}'.format(datefilm), 
        'current_events':'//div[@id="events-block"]',
        'events_list':'ul[@class="b-lists list_afisha col-5"]', 
        'film_name':'.//a[@class="name"]/span//text()',
         }

        tree = html.fromstring(requests.get(movies_params['url']).text)

        current_events = tree.xpath(movies_params['current_events'])[0]
        events_list = current_events.xpath(movies_params['events_list'])


        def create_movies_list():
            movies_list = []

            for movies_block in events_list:

                for movie in movies_block:

                    movies_list += [movie.xpath(movies_params['film_name'])[0]]

            return movies_list


        return render_template('movies.html', movies = create_movies_list())

    else:
        return render_template('movies.html' , movies = 'Выберите дату')










@cursy.route('/')

def cursy():
	return render_template('curs.html')





	