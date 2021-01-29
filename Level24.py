from PIL import Image

maze = Image.open("maze.png")
directions = [(0,1), (0,-1), (1,0), (-1,0)]
white = (255, 255, 255, 255)
w, h = maze.size
entrance = (w - 2, 0)
exitpoint = (1, h - 1)

next_map = {}

queue = [exitpoint]

while queue:
    pos = queue.pop(0)
    if pos == entrance:
        break
    for d in directions:
        tmp = (pos[0] + d[0], pos[1] + d[1])
        if not tmp in next_map and 0 <= tmp[0] < w and 0 <= tmp[1] < h and maze.getpixel(tmp) != white:
            next_map[tmp] = pos
            queue.append(tmp)

path = []
while pos != exitpoint:
    path.append(maze.getpixel(pos)[0])
    pos = next_map[pos]

# skipping the 0s
print(path)
print(path[1::2])
open('maze.zip','wb').write(bytes(path[1::2]))