from PIL import Image, ImageChops

image = Image.open("mozart.gif")

# print(image.histogram())

# tmp = image.copy()
# tmp.frombytes(bytes([60] * (tmp.height * tmp.width)))
# tmp.show()


import numpy as np
shifted = [bytes(   np.roll(    row, -row.tolist().index(195)   ).tolist()     ) for row in np.array(image)]

Image.frombytes(image.mode, image.size, b"".join(shifted)).show()