with open(__file__[:-2]+"txt", "r") as f:
    maze = list(map(str.strip, f.readlines()))

print(maze)

print([x for x in ''.join(maze) if x not in ".#"])
print(len(maze), len(maze[0]))


paths = [(0,0, code)]
minpath = maxpath = None

height = len(maze)
while len(paths):
    x, y, path = paths.pop(0)
    if x < 0 or x > 3 or y < 0 or y > 3:
        continue
    if x == 3 and y == 3:
        if not minpath:
            minpath = path
        maxpath = path
        continue
    doors = open_doors(path)
    for d in DIRS:
        if doors[d]:
            xd, yd = OFFSETS[d]
            paths.append((x+xd, y+yd, path+d))

print("min", minpath)
print("max", len(maxpath[8:]), maxpath[8:])

