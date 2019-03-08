
import requests


def get_wether_today():
	url = 'https://samples.openweathermap.org/data/2.5/weather?q=Minsk&appid=812e89737fcf7992cc92812abee5c137'

	r = requests.get(url).json()
	
	city = r['name']
	weather = r['main']
	return str(city), str(weather)


def get_rate_today_usd():
	
	usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
	
	response = requests.get(usd).json()
	
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(name), str(price)
	 

def get_rate_today_rub():
	
	rub = 'http://www.nbrb.by/API/ExRates/Rates/298'
	
	response = requests.get(rub).json()

	scale = response['Cur_Scale']
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(scale),str(name),str(price)

def get_rate_today_uah():
	
	uah = 'http://www.nbrb.by/API/ExRates/Rates/290'
	
	response = requests.get(uah).json()
	
	scale = response['Cur_Scale']
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(scale),str(name),str(price)

def get_rate_today_eur():
	
	eur = 'http://www.nbrb.by/API/ExRates/Rates/292'
	
	response = requests.get(eur).json()
	
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(name),str(price)

def get_rate_today_pln():
	
	pln = 'http://www.nbrb.by/API/ExRates/Rates/293'
	
	response = requests.get(pln).json()

	scale = response['Cur_Scale']
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	return str(scale),str(name),str(price)

