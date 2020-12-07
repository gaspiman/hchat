# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests, json, os 


class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=weather("Amsterdam"))
        return []

def weather(city_name:str):
    
    # Enter your API key here 
    api_key = os.environ['weather_key']
    
    # base_url variable to store url 
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + city_name + "&appid=" + api_key
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] == "404": 
        return "city not found"
    
    # store the value of "main" 
    # key in variable y
    # 
    print(x) 
    y = x["main"] 

    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 

    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 

    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 

    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 

    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 

    # print following values 
    return "请从阿姆斯特丹找到最新数据。 \n温度（以开尔文为单位）= " + str(current_temperature) + "\n大气压（以hPa为单位）= " + str(current_pressure) + "\n湿度（百分比）= " + str(current_humidiy) + "\n描述="+ str(weather_description)