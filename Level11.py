import urllib.request

url="http://www.pythonchallenge.com/pc/return/cave.jpg"

urllib.request.urlretrieve (url, url.split('/')[-1])


#open(url.split('/')[-1], 'wb').write(r.content)