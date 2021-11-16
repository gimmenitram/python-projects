import requests

api_key = "" # Enter Key
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)
json = request.json()
#print(json)

description = json.get("weather")[0].get("description")
print("Today's forecast is", description)
max_temp = json.get("main").get("temp_max")
low_temp = json.get("main").get("temp_min")
print("Today's high is ", max_temp, ", and low is ", low_temp)