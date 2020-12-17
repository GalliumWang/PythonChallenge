import base64, wave, array

# Input ...

h = open("data_L19.txt")
# print(base64.b64decode(h.read()))

tmp=base64.b64decode(h.read())

a = array.array("u", tmp)

print(len(tmp))

a.byteswap()

print(len(a))

h.close()

# ... Processing ...

h = wave.open("modified.wav", "wb")
h.setnchannels(1)
h.setsampwidth(1)
h.setframerate(22050)

# ... Output

h.writeframes(a.tostring())
h.close()