from itertools import  permutations

with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))


def swap(password, args):
    if args[0] == "position":
        a, b = int(args[1]), int(args[4])
    else:
        c, d = args[1], args[4]
        a, b = password.index(c), password.index(d)
    password[a], password[b] = password[b], password[a]
    return password


def rotate(password, args):
    if args[0] == 'based':
        steps = password.index(args[5])
        steps += 2 if steps >= 4 else 1
        steps %= len(password)
    else:
        steps = int(args[1])
        if args[0] == "left":
            steps = -steps
    return password[-steps:] + password[:-steps]


def move(password, args):
    from_pos = int(args[1])
    to_pos = int(args[4])
    save_char = [password[from_pos]]
    password = password[:from_pos] + password[from_pos+1:]
    password = password[:to_pos] + save_char + password[to_pos:]
    return password


def reverse(password, args):
    from_pos = int(args[1])
    to_pos = int(args[3]) + 1
    return password[:from_pos] + password[from_pos:to_pos][::-1] + password[to_pos:]


CMD_DICT = {'swap' : swap, 'rotate' : rotate, 'move' : move, 'reverse' : reverse}


def encrypt(password, lines):
    password = list(password)
    for line in lines:
        # print(line)
        cmd, *args = line.split()
        password = CMD_DICT[cmd](password, args)

    return ''.join(password)


def crack(password, lines):
    password_list = permutations(password)
    for p in password_list:
        if encrypt(p, lines) == password:
            return ''.join(p)
    return None


print("p =", encrypt("abcdefgh", lines))
print("c =", crack('fbgdceah', lines))
