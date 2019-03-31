
import requests
from datetime import datetime

def get_weather_today():
	city_name = "в Минске"
	city_id = 625144
	appid = "812e89737fcf7992cc92812abee5c137"
	
	res = requests.get("http://api.openweathermap.org/data/2.5/weather",
	    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
	data = res.json()
	
	rasvet = data['sys']['sunrise']	
	voshod = datetime.fromtimestamp(rasvet).strftime('%Y-%m-%d %H:%M:%S')
	zakat = data['sys']['sunset']	
	nzakat = datetime.fromtimestamp(zakat).strftime('%Y-%m-%d %H:%M:%S')
	
	weather = ["Сегодня "+str(city_name)+': '+str(data['weather'][0]['description'])+',   '+ 'Скорость ветра:  '+str(data['wind']['speed'])+' '+'м/с, '+"направление:  "+str(data['wind']['deg'])+',   '+"Атмосферное давление:   "+str(data['main']['pressure'])+' гПа,   '+"Влажность:   "+str(data['main']['humidity'])+'%,   '+"Температура воздуха:  "+str(data['main']['temp']) +',   '+ "минимальная температура:  "+ str(data['main']['temp_min']) +',   '+ "максимальная температура:  "+str(data['main']['temp_max'])+',   '+"восход:  "+str(voshod)+',   '+"закат:  "+str(nzakat)]
	return weather
	




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

