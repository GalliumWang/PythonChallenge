import re
import urllib
import requests

baseURL="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

startURL="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66081"


while(True):
    htmlText=requests.get(startURL).text

    matchGroup=re.findall("[0-9]{1,5}",htmlText)

    if(len(matchGroup)>0):
        startURL=baseURL+matchGroup[-1]
    else:
        print(htmlText)
        break


