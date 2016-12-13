
FAVE = 1364

# 0 empty, 1 wall

def cell(x, y):
    v = x*x + 3*x + 2*x*y + y + y*y + FAVE
    digits = map(int, bin(v)[2:])
    return sum(digits) % 2

DIM_X = 40
DIM_Y = 40

maze = [['#' if cell(x,y) else '.' for x in range(DIM_X)] for y in range(DIM_Y)]

print '\n'.join(map(''.join, maze))

node_queue = [((1, 1), 0)]

node_distance = {}

DEST = (31,39)

while True:
    (x,y), dist = node_queue.pop(0)
    if x >= 0 and y >= 0 and cell(x, y) == 0 and not (x,y) in node_distance:
        # print node_distance
        if (x, y) == DEST:
            print x, y, dist
            break
        node_distance[(x,y)] = dist
        node_queue.append(((x+1, y), dist +1))
        node_queue.append(((x-1, y), dist +1))
        node_queue.append(((x, y+1), dist +1))
        node_queue.append(((x, y-1), dist +1))

print len([x for x in node_distance.values() if x <= 50])