# python2 only

from collections import *
from string import ascii_lowercase
import string

strrr="map"

alphalList=[]

for i in ascii_lowercase:
    alphalList.append(i)

alphalList2=[]

for i in range(26):
    alphalList2.append(alphalList[(i+2)%26])

fStr="".join(alphalList)
fStr2="".join(alphalList2)

print(strrr.translate(string.maketrans(fStr,fStr2)))

