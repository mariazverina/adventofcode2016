import inspect

with open(__file__[:-2]+"txt", "r") as f:
    lines = map(str.split, f.readlines())

print lines

registers = dict(zip(list("abcd"), [0]*4))
pc = 0

def value(reg_or_literal):
    if reg_or_literal in registers:
        x = registers[reg_or_literal]
    else:
        x = int(reg_or_literal)
    return x

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
    instructions[word[0]](*word[1:])
    pc += 1



