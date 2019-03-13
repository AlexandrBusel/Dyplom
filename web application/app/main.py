from app import app
import view
import requests

@app.route('/curs')
def curs():
		
	usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
			
	response = requests.get(usd).json()
		
	name = response['Cur_Name']
	price = response['Cur_OfficialRate']
	u = str(name) +' - '+ str(price)
	return str(u)

	

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



if __name__ == '__main__':
	app.run()