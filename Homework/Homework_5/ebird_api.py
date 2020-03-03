# import http.client
# import mimetypes

# conn = http.client.HTTPSConnection("api.ebird.org")
# payload = ''
# headers = {
#   'X-eBirdApiToken': '{{X-vev5bd57v7ou}}'
# }
# conn.request("GET", "/v2/data/obs/US/recent/notable?detail=full", payload, headers)
# res = conn.getresponse()
# data = res.text()
# print(data.decode("utf-8"))

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
