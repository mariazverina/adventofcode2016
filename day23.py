from collections import defaultdict

with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.split, f.readlines()))


registers = dict(list(zip(list("abcd"), [0]*4)))
pc = 0


def value(reg_or_literal):
    if isinstance(reg_or_literal, str):
        return registers[reg_or_literal]
    return reg_or_literal


def cpy(*params):
    registers[params[1]] = value(params[0])


def inc(*params):
    registers[params[0]] += 1


def dec(*params):
    registers[params[0]] -= 1


def zer(*params):
    registers[params[0]] = 0


def add(*params):
    registers[params[0]] += value(params[1])


def mul(*params):
    registers[params[0]] *= value(params[1])


def jnz(*params):
    global pc
    if value(params[0]) != 0:
        pc += value(params[1]) - 1 # subtract one because pc is always incremented


def tgl(*params):
    global lines, toggle_map
    ipc = pc + value(params[0])
    if ipc >= len(lines):
        return
    lines[ipc][0] = toggle_map[lines[ipc][0]]

instructions = dict(list(zip("cpy inc dec jnz tgl add zer mul".split(), [cpy, inc, dec, jnz, tgl, add, zer, mul])))
toggle_map = {cpy: jnz, jnz: cpy, inc: dec, dec: inc, tgl: inc}

def precompile(xs):
    global instructions
    xs[0] = instructions[xs[0]]
    for i in range(1, len(xs)):
        try:
            xs[i] = int(xs[i])
        except:
            pass


list(map(precompile, lines))
print(lines)

registers['a'] = 12

while True:
    if pc >= len(lines) and pc < 100:
        print(registers)
        break
    word = lines[pc]
    # print(word)
    word[0](*word[1:])
    # print(registers, pc) #, list(zip(range(100), lines)))
    pc += 1



