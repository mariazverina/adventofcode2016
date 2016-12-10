

# north is 0, east is 1 ....

DIR = {'R': 1, 'L': -1 }
def apply(sleighDistance, instruction):
    turn, distance = instruction
    heading, accumulator = sleighDistance
    heading += DIR[turn]
    heading %= 4
    accumulator[heading] += distance
    return (heading, accumulator)


with open("day1.txt", "r") as f:
    line = f.readline()

tokens = line.split(", ")
instructions = map(lambda x:(x[0], int(x[1:])), tokens)

# part 1
h, dist_matrix =  reduce(apply, instructions, (0, [0,0,0,0]))
print abs(dist_matrix[0] - dist_matrix[2]) + abs(dist_matrix[1] - dist_matrix[3])


