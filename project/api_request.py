# import requests
# import json
#
# url = "http://127.0.0.1:8000/api/api/"
# payload = json.dumps({
#     "city": "Craiova",
#     "country": "Romania"
# })
# headers = {
#     "Content-Type": "application/json"
# }
# response = requests.request("GET", url, headers=headers, data=payload)
# print(response.json())
import requests

url = "https://v6.exchangerate-api.com/v6/5698482ba11f4b5424f52c63/latest/RON"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()["conversion_rates"]["RON"])
