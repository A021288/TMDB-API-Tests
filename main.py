import requests
from config import BASE_URI, API_KEY

payload = {
    "api_key": API_KEY,
    "page": 1
}
resource_url = BASE_URI + "movie/top_rated"
response = requests.get(resource_url, params=payload)

response.status_code
print("hhhhhhh")
print(response)
print(response.json().keys())

