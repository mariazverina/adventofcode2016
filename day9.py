with open(__file__[:-2]+"txt", "r") as f:
    line = f.readline().strip()

def tokenize(line):
    if line[0] == '(':
        ix = line.index(')')
        repeater = tuple(map(int, line[1:ix].split('x')))
        return repeater, line[ix+1:]

    ix = line.find('(')
    if ix < 0:
        return line, ""
    return (line[:ix], line[ix:])


def file_len(line):
    total_len = 0
    while len(line):
        token, line = tokenize(line)
        if isinstance(token, tuple):
            symbol_len, repeat_count = token
            total_len += file_len(line[:symbol_len]) * repeat_count
            line = line[symbol_len:]
        else:
            total_len += len(token)

    return total_len


print(file_len(line))