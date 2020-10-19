import urllib, zipfile, re, collections

o, n, f = [], "90052", "%s.txt"

nnr = "Next nothing is (\d+)"

# Download the ZIP file from http://www.pythonchallenge.com/pc/def/channel.zip to ./channel.zip

file = zipfile.ZipFile("channel.zip")

o.append(file.getinfo(f % n).comment)

while True:
    try:
        n = re.search(nnr, file.read(f % n)).group(1)
    except:
        print file.read(f % n)
        break
    #print(file.getinfo(f % n).comment)
    o.append(file.getinfo(f % n).comment)

print "".join(o)