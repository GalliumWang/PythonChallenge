import re

oriStr=str(open("./Level3Text.txt").read())

reStr=""

for i in (re.findall('[^A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z]',oriStr)):
    reStr+=i

print(reStr)