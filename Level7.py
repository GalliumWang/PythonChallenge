from PIL import Image

im=Image.open("./oxygen.png")
print(im.size,im.mode)

letterList=[]

HEIGHT=43

for i in range(1,630,7):
    letter=im.getpixel((i,HEIGHT))[0]
    letterList.append(chr(letter))

print("".join(letterList))

#ans:integrity