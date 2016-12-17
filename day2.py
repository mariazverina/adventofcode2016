with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

KEYPAD = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]

class Digit:
    def go_r(self):
        max_val = 4 - abs(self.y - 2)
        if self.x < max_val:
            self.x += 1

    def go_l(self):
        min_val = abs(self.y - 2)
        if self.x > min_val:
            self.x -= 1

    def go_u(self):
        min_val = abs(self.x - 2)
        if self.y > min_val:
            self.y -= 1

    def go_d(self):
        max_val = 4 - abs(self.x - 2)
        if self.y < max_val:
            self.y += 1

    def __init__(self):
        self.funmap = {'U' : self.go_u, 'D' : self.go_d, 'R' : self.go_r, 'L' : self.go_l}
        self.x = 1
        self.y = 1

    def decode(self, instructions):
        for d in instructions:
            self.funmap[d]()
        return KEYPAD[self.y][self.x]


d = Digit()
for line in lines:
    print(d.decode(line))