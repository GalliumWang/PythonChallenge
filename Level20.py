import urllib.request, base64
import re

request = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
cred = base64.b64encode(b"butter:fly")
request.add_header("Authorization", "Basic %s" % cred.decode())
print(request.headers)
# {'Authorization': 'Basic YnV0dGVyOmZseQ=='}

response = urllib.request.urlopen(request)
print(response.headers)


pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')
content_range = response.headers['content-range']
(start, end, length) = pattern.search(content_range).groups()
request.headers['Range'] = 'bytes=%i-' % (int(end) + 1)

print('bytes=%i-' % (int(end) + 1))

response = urllib.request.urlopen(request)
print(response.headers)
# {'Authorization': 'Basic YnV0dGVyOmZseQ=='}
# Content-Type: application/octet-stream
# Content-Transfer-Encoding: binary
# Content-Range: bytes 30203-30236/2123456789
# Connection: close
# Transfer-Encoding: chunked
# Server: lighttpd/1.4.35

print(response.read().decode())
# Why don't you respect my privacy?