import requests
from bs4 import BeautifulSoup

def get_html(url):
	response = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
	html = response.text
	return html

def get_weather_now(text):
	url = "https://pogoda.mail.ru/prognoz/moskva/24hours/"
	html = get_html(url)
	soup = BeautifulSoup(html, 'html.parser')
	forecast_items = soup.find_all('span', class_="p-forecast__data")

	"**************'description'**************"
	description = soup.find('span', class_="p-forecast__description").text

	"**************'temperature'**************"
	temp_now = soup.find('span', class_="p-forecast__temperature-value").text
	temp_feel_now = forecast_items[0].text

	"***************'pressure'****************"
	pressure = forecast_items[1].text

	"****************'wind'*******************"
	wind_speed = forecast_items[2].text[:forecast_items[2].text.find('/') + 2]
	wind_dir = forecast_items[2].text[forecast_items[2].text.find('/') + 2:]

	"***************'humidity'**************"
	humidity = forecast_items[3].text

	"***************'rain probability'**************"
	rain_probability = 0
	cntr = 0
	for el in forecast_items:
		if el.text[-1] == '%':
			cntr += 1
			if cntr == 3:
				rain_probability = el.text


	forecast = {"Описание": description,
				"Температура": temp_now,
				"Ощущается как": temp_feel_now,
				"Давление": pressure,
				"Скорость ветра": wind_speed,
				"Направление ветра": wind_dir,
				"Влажность": humidity,
				"Вероятность осадков": rain_probability
	}

	return forecast

forecast = get_weather_now('a')
