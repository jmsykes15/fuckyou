import urllib2
import json

#state = "NY"
#city = "New_York"
f = urllib2.urlopen('http://api.wunderground.com/api/4fe95a34faa23e98/forecast/q/NY/New_York.json')
json_string = f.read()
parsed_json = json.loads(json_string)

x = json.loads(json.dumps(parsed_json['forecast']['simpleforecast']['forecastday']))

print  x[0]['conditions']
f.close()
