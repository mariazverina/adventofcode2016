with open(__file__[:-2]+"txt", "r") as f:
    lines = map(str.strip, f.readlines())

print lines