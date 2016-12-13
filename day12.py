import inspect

with open(__file__[:-2]+"txt", "r") as f:
    lines = map(str.split, f.readlines())

def parse_ints(xs):
    for i in range(len(xs)):
        try:
            xs[i] = int(xs[i])
        except:
            pass

map(parse_ints, lines)
print lines


registers = dict(zip(list("abcd"), [0]*4))
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


def jnz(*params):
    global pc
    if value(params[0]) != 0:
        pc += int(params[1]) - 1 # subtract one because pc is always incremented

instructions = dict(zip("cpy inc dec jnz".split(), [cpy, inc, dec, jnz]))

registers['c'] = 1

while True:
    if pc >= len(lines) and pc < 100:
        print registers
        break
    word = lines[pc]
    # print word
    instructions[word[0]](*word[1:])
    # print registers, pc
    pc += 1



