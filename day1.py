from functools import reduce


# north is 0, east is 1 ....

DIR = {'R': 1, 'L': -1 }
OFFSET = ((0, 1), (1, 0), (0, -1), (-1, 0))

def make_turn(heading, turn):
    heading += DIR[turn]
    return heading % 4



def apply(sleigh_state, instruction):
    turn, distance = instruction
    heading, accumulator = sleigh_state
    heading = make_turn(heading, turn)
    accumulator[heading] += distance
    return (heading, accumulator)


with open("day1.txt", "r") as f:
    line = f.readline()

tokens = line.split(", ")
instructions = [(x[0], int(x[1:])) for x in tokens]

# part 1
h, dist_matrix =  reduce(apply, instructions, (0, [0,0,0,0]))
print(abs(dist_matrix[0] - dist_matrix[2]) + abs(dist_matrix[1] - dist_matrix[3]))

# part 2
print(instructions)

direction = 0
visited = set((0, 0))
location = (0, 0)

for (turn, distance) in instructions:
    direction = make_turn(direction, turn)
    x, y = location
    a, b = OFFSET[direction]
    for d in range(1, distance + 1):
        point = x + d * a, y + d * b
        if point in visited:
            print(point, sum(map(abs,point)))
            exit(0)
        else:
            visited.add(point)
        print(point)
    location = point


print(visited)
    # print direction, distance



