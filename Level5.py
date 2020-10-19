#python 2.x only

import urllib,pickle

url="http://www.pythonchallenge.com/pc/def/banner.p"

dataStream=urllib.urlopen(url)

data=pickle.load(dataStream)

#print(data)

for elt in data:
    print "".join([e[1] * e[0] for e in elt])
    #channel