from app import app
import view
import requests

@app.route('/curs')
def curs():
		
	usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
	res_u = requests.get(usd).json()
	name_u = res_u['Cur_Name']
	price_u = res_u['Cur_OfficialRate']
	u = str(name_u) +' - '+ str(price_u)


	eur = 'http://www.nbrb.by/API/ExRates/Rates/292'
	res_e = requests.get(eur).json()
	name_e = res_e['Cur_Name']
	price_e = res_e['Cur_OfficialRate']
	e = str(name_e) +' - '+ str(price_e)


	rub = 'http://www.nbrb.by/API/ExRates/Rates/298'
	res_r = requests.get(rub).json()
	scale_r = res_r['Cur_Scale']
	name_r = res_r['Cur_Name']
	price_r = res_r['Cur_OfficialRate']
	r =str(scale_r)+' '+str(name_r) +' - '+ str(price_r)


	uah = 'http://www.nbrb.by/API/ExRates/Rates/290'
	res_uh = requests.get(uah).json()
	scale_uh = res_uh['Cur_Scale']
	name_uh = res_uh['Cur_Name']
	price_uh = res_uh['Cur_OfficialRate']
	uh =str(scale_uh)+' '+str(name_uh) +' - '+ str(price_uh)


	pln = 'http://www.nbrb.by/API/ExRates/Rates/293'
	res_p = requests.get(pln).json()
	scale_p = res_p['Cur_Scale']
	name_p = res_p['Cur_Name']
	price_p = res_p['Cur_OfficialRate']
	p = str(scale_p)+' '+str(name_p) +' - '+ str(price_p)


	return str(u) +';   '+ str(e)+';   '+str(r)+';   '+str(uh)+';   '+str(p)

	

@app.route('/pogoda')
def pogoda():

	city_name = "в Минске"
	city_id = 625144
	appid = "812e89737fcf7992cc92812abee5c137"
	
	res = requests.get("http://api.openweathermap.org/data/2.5/weather",
	    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
	data = res.json()
	# return str(data)
	weather = str(city_name)+': '+str(data['weather'][0]['description'])+' '+"Температура воздуха"+': '+str(data['main']['temp']) +', '+ "минимальная температура:"+' '+ str(data['main']['temp_min']) +', '+ "максимальная температура:"+' '+str(data['main']['temp_max'])
	return str(weather)



@app.route('/films')
def films():
	movies_params = {

	'url':'https://afisha.tut.by/film/', 

	'current_events':'//div[@id="events-block"]',

	'events_list':'ul[@class = "b-lists list_afisha col-5"]',

	'film_name':'.//a[@class = "name"]/span//text()',
	}

	class MoviesList:
	
		tree = requests.get(movies_params['url']).text

		current_events = movies_params['current_events'][0]
		events_list = current_events[movies_params['events_list']]
		

		def create_movies_list(self):
			movies_list = []
		
			for movies_block in self.events_list:
			
				for movie in movies_block:
					movies_list+=movies_params['film_name'][0]
		
			return movies_list
	# return MoviesList().create_movies_list()


if __name__ == '__main__':
	app.run()