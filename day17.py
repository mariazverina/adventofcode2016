import hashlib
from collections import Counter

OFFSETS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
DIRS = list("UDLR")
print(DIRS, OFFSETS)

def md5(s):
    # global MD5_CACHE
    # if s in MD5_CACHE:
    #     return MD5_CACHE[s]
    #
    d = s
    # for i in range(2017):
    h = hashlib.md5()
    h.update(d.encode())
    d = h.hexdigest()
    # MD5_CACHE[s] = d
    return d

def open_doors(s):
    s = md5(s)[:4]
    return dict(zip(DIRS, [x > "a" for x in s]))


# code = "ihgpwlah"
# code = "kglvqrro"
# code = "ulqzkmiv"
code = "vkjiggvb"

paths = [(0,0, code)]
minpath = maxpath = None

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


