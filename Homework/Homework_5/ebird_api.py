import requests

url = "https://api.ebird.org/v2/data/obs/US/recent"

payload = {
	"back": '{{30}}'
}
headers = {
  'X-eBirdApiToken': '{{x-vev5bd57v7ou}}'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
print(response.status_code)
