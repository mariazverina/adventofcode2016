from itertools import permutations

with open(__file__[:-2]+"txt", "r") as f:
    maze = list(map(str.strip, f.readlines()))

# maze = """###########
# #0.1.....2#
# #.#######.#
# #4.......3#
# ###########""".split()
#

print(len(maze[0]), "x", len(maze))

height = len(maze)
width = len(maze[0])
locations = {maze[y][x]:(x,y) for y in range(height) for x in range(width) if maze[y][x] not in ".#"}
print("locations", locations)

mindists = {}

for source in locations.keys():
    mindists[source] = {}
    paths = [tuple(list(locations[source]) + [0])]
    visited = set()
    while len(mindists[source]) < len(locations) and len(paths):
        x, y, dist = paths.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x,y))
        if x < 0 or x >= width or y < 0 or y >= height:
            continue
        cell = maze[y][x]
        if cell == '#':
            continue
        if cell != '.':
            # we found a target
            if cell not in mindists[source]:
                mindists[source][cell] = dist

        for a,b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if not (a,b) in visited:
                paths.append((a,b,dist+1))


print(mindists)

dests = list(locations.keys())
dests.remove('0')

def eval_path(path):
    global mindists
    src = '0'
    d = 0
    for n in path:
        d += mindists[src][n]
        src = n
    return (d, path)

paths = list(permutations(dests))

# part 1
print(sorted(map(eval_path, paths))[:5])
# part 2
print(sorted(map(lambda x:eval_path(list(x)+['0']), paths))[:5])

