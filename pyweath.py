#!/usr/bin/python
# vim: set fileencoding=UTF-8 :

import urllib2
import json

state = "NY"
city = "New_York"

def weather():
    url = urllib2.urlopen('http://api.wunderground.com/api/4fe95a34faa23e98/forecast/q/' + state + '/'+ city +'.json')
    json_string = url.read()
    parsed_json = json.loads(json_string)
    f = json.loads(json.dumps(parsed_json['forecast']['simpleforecast']['forecastday']))

    return {
    	'current_condition': f[0]['conditions'],
	'current_temp': f[0]['high']['celsius'],
	'wind': f[0]['maxwind']['kph'],
	'humidity': f[0]['avehumidity'],
	'forecasts': f[1],
    }



def main():
    a=weather()
    print '├ Temperature:',a['current_temp'],'°C'
    print '├ Condition  :',a['current_condition']
    print '├ Wind Speed :',a['wind'], 'km/h'
    print '├ Humidity   :',a['humidity'], '%'
    print '├ Tomorrow   :',a['forecasts']['date']['monthname_short'],a['forecasts']['date']['day']
    print '├ Highs      :',a['forecasts']['high']['celsius'],'°C'
    print '├ Lows       :',a['forecasts']['low']['celsius'],'°C'
    print '├ Sky        :',a['forecasts']['conditions']

main()
