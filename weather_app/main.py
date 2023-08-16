import requests
import json
import pyttsx3
city=input("Enter the name of the city \n")
url=f"http://api.weatherapi.com/v1/current.json?key=49ca892080274a0296965642230908&q={city}"
resp=requests.get(url)
print(resp.text)
wdic= json.loads(resp.text)
temp=wdic["current"]["temp_c"]
temp2=wdic["location"]["region"]
temp3=wdic["location"]["localtime"]
engine = pyttsx3.init()
print(temp2)
engine.say(f"the current weather at {city} is {temp} degrees")
engine.say(f"the {city} is under {temp2} region")
engine.say(f"the locan time at {city} is {temp3}")
engine.runAndWait()

