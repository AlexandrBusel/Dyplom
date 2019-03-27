
import requests

import lxml
from lxml import html
from flask import request
from flask import render_template


movies_params = {

'url':'https://afisha.tut.by/film/', 

'current_events':'//div[@id="events-block"]',

'events_list':'ul[@class = "b-lists list_afisha col-5"]',

'film_name':'.//a[@class = "name"]/span//text()',
}

class MoviesList:

	tree = html.fromstring(requests.get(movies_params['url']).text)

	current_events = tree.xpath(movies_params['current_events'])[0]
	events_list = current_events.xpath(movies_params['events_list'])
		

	def create_movies_list(self):
		movies_list = []
		
		for movies_block in self.events_list:
			
			for movie in movies_block:
				movies_list+=[movie.xpath(movies_params['film_name'])[0]]
		
		return movies_list




        