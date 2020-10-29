import requests

url="http://www.pythonchallenge.com/pc/return/cave.jpg"

r = requests.get(url)

print(r.headers.get('content-type'))

#open(url.split('/')[-1], 'wb').write(r.content)