import requests

city=input("Enter the name of the city \n")
url=f"http://api.weatherapi.com/v1/current.json?key=49ca892080274a0296965642230908&q={city}"
resp=requests.get(url)
print(resp.text)
