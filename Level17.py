from urllib.request import urlopen
from urllib.parse import unquote_plus, unquote_to_bytes
import re, bz2


num ='12345'
info = ''
while(True):
    h = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+num)
    raw = h.read().decode("utf-8")
    print(raw)
    cookie = h.getheader("Set-Cookie")
    info += re.search('info=(.*?);', cookie).group(1)
    match = re.search('the next busynothing is (\d+)', raw)
    if match == None: 
        break
    else:
        num = match.group(1)



#print(info)
res = unquote_to_bytes(info.replace("+", " "))

print(unquote_plus(info))

print(res)
print(bz2.decompress(res).decode())