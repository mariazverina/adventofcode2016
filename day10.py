
class Value:
    def __init__(self, desc):
        tokens = desc.split(' ')
        self.val = int(tokens[1])
        self.bot = int(tokens[5])

    def __repr__(self):
        return repr((self.val, self.bot))

class RobotTroupe:
    def __init__(self):
        self.robots = {}
        self.io = {}

    def register(self, robot):
        self.robots[robot.id] = robot

    def load_value(self, value, dest_robot_id, io):
        if io:
            self.io[dest_robot_id] = value
        else:
            self.robots[dest_robot_id].push(value)

class Robot:
    def __init__(self, desc, troupe):
        tokens = desc.split(' ')
        self.id = int(tokens[1])
        self.low = int(tokens[6])
        self.high = int(tokens[11])
        self.iolow = tokens[5] == "output"
        self.iohigh = tokens[10] == "output"
        self.value1 = None
        self.troupe = troupe
        troupe.register(self)

    def __repr__(self):
        return repr((self.id, self.low, self.high, self.value1))

    def push(self, value):
        if self.value1 is None:
            self.value1 = value
            return
        print(self, value)
        troupe.load_value(min(value, self.value1), self.low, self.iolow)
        troupe.load_value(max(value, self.value1), self.high, self.iohigh)




with open("day10.txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

troupe = RobotTroupe()
values = [Value(x) for x in lines if x[0] == 'v']
print(values)
bots = [Robot(x, troupe) for x in lines if x[0] == 'b']
print(sorted(bots, key=lambda r:r.id))


for v in values:
    troupe.load_value(v.val, v.bot, False)

print(troupe.io)
print(troupe.io[0] * troupe.io[1] * troupe.io[2])
