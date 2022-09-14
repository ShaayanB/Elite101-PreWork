import requests, json
import random

# https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# https://api.openweathermap.org/

def main():

  print("Hello! I am the weather chat bot!")

  goodresponses = ["good!", "great!", "awesome to hear!", "super!", "fantastic!"]
  
  doing = input("How are you doing? ")
  print(random.choice(goodresponses))
  convo()
  
  while True:
    again = input("Do you want to ask again? ")
    if 'y' in again:
      convo()
    else:
      print("Thanks for interacting!")
      break
  

def convo():
  question = input("Ask me about the temperature, humidity, or pressure in any city! (format: What is the ___ in ___?) ")

  words_list = question.split(" ")
  city = words_list[5]
  item = words_list[3]

  # city = "austin"
  # item = "temperature"  #temperature, pressure, humidity, weather
  response = get_weather_item(city, item)
  print(item + " in " + city + " is:\n" + str(response))

def get_weather_item(city, item):
    response_json = get_weather_json(city)
    item_desc = "Can not find the City " + city

    if response_json["cod"] != "404":
        main = response_json["main"] 
        if (item == "temperature"):
            item_desc = str(kelvin_to_F(main["temp"]))+ " F"
        elif (item == "pressure"):
            item_desc = str(main["pressure"]) + " hPa"
        elif (item == "humidity"):
            item_desc = str(main["humidity"]) + " %"
        else:
            item_desc = str(response_json["weather"])

    return(item_desc)

def kelvin_to_F(value):
    return round(value * 1.8 - 459.67,0)

def get_weather_json(city):
    link = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=187306b320789bb927abf9599c3db9a7"
    response = requests.get(link)
    return(json.loads(response.text))  #convert to string

if __name__ == "__main__":
    main()