# import urllib library
# import json
import json

from urllib.request import urlopen

import requests

# Defined url with json content and issued to variable called 'url'
url = "https://mocki.io/v1/1f02b848-65cc-4672-8708-fd139678a7ea"

# Defiened url we will send our new data
url_to_send = "https://httpbin.org/post"

# store the response of URL thank of our
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print(data_json)

# for loop which takes name properties from json file
for item in data_json:
    names = item['name']
    data_to_send = names
    print(data_to_send)
    r = requests.post(url_to_send, json=data_to_send)
    print(r.text)
