
import requests


def get_weather_today():
	city_name = "в Минске"
	city_id = 625144
	appid = "812e89737fcf7992cc92812abee5c137"
	
	res = requests.get("http://api.openweathermap.org/data/2.5/weather",
	    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
	data = res.json()
	return ("Сегодня:", city_name),	("состояние погоды:", data['weather'][0]['description']), ("Температура воздуха:", data['main']['temp']), ("минимальная температура:", data['main']['temp_min']), ("максимальная температура:", data['main']['temp_max'])	
	

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

