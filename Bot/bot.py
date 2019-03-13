
import requests

import misc
from comands import get_rate_today_usd, get_rate_today_rub, get_rate_today_eur, get_rate_today_uah, get_rate_today_eur,get_rate_today_pln, get_weather_today
from movie_parser import MoviesList

from time import sleep


token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'


global last_update_id
last_update_id = 0


def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()

def get_message():

	data = get_updates()
	last_object = data['result'][-1]

	update_id = last_object['update_id']

	global last_update_id
	if last_update_id != update_id:
		last_update_id = update_id

		chat_id = last_object['message']['chat']['id']
		message_text = last_object['message']['text']

		message = {'chat_id': chat_id,
					'text': message_text}
		return message	
	return None			

def send_message(chat_id, text='Wait a second, please...'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	
	requests.get(url)

def main():
	
	while True:
		answer = get_message()

		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']
			
			
			if text == 'курсы':
				send_message(chat_id, get_rate_today_usd())
				send_message(chat_id, get_rate_today_eur())
				send_message(chat_id, get_rate_today_rub())
				send_message(chat_id, get_rate_today_uah())
				send_message(chat_id, get_rate_today_pln())
				

			if text == 'погода':
				send_message(chat_id, get_weather_today())

			
			if text == 'кино сегодня':
				send_message(chat_id, MoviesList().create_movies_list())
		else:
			continue

		sleep(6) 			


if __name__ == '__main__':
	main()

	