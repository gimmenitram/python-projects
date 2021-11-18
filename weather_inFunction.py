import requests

def getWeatherDescTemp():
    api_key = "" # Enter Key
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")

    max_temp = json.get("main").get("temp_max")
    low_temp = json.get("main").get("temp_min")

    return {'desc': description,
            'high': max_temp,
            'low': low_temp}

def main():
    weatherDict = getWeatherDescTemp()
    print("Today's forecast is", weatherDict.get('desc'))
    print("Today's high is ", weatherDict.get('high'), ", and low is ", weatherDict.get('low'))

main()