import requests

url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"

querystring = {"term":"bojack","country":"uk"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)