import numpy as np
with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

disp = np.zeros((6,50))

def rotate(args):
    offset = int(args[3])
    ix = int(args[1].split('=')[1])

    if args[0] == "row":
        disp[ix, :] = np.roll(disp[ix, :], offset)
    else:
        disp[:, ix] = np.roll(disp[:, ix], offset)


def rect(args):
    width, height = list(map(int, args[0].split('x')))
    disp[:height, :width] = 1

FUNMAP = {'rotate' : rotate, 'rect' : rect}

for line in lines:
    words = line.split(" ")
    FUNMAP[words[0]](words[1:])

print(sum(sum(disp)))
print('\n'.join([''.join(['X' if x else '.' for x in row] ) for row in disp]))

