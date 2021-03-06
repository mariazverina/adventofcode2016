import re

with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))


def has_abba(token):
    if len(token) < 4:
        return False
    quads = list(zip(token, token[1:], token[2:], token[3:]))
    mult = -1 if token[0] == '[' else 1
    return max([1 if b == c and a == d and a != b else 0 for (a, b, c, d) in quads]) * mult

def supports_tls(votes):
    votes = set(votes)
    if -1 in votes:
        return False
    return max(votes)

def supports_ssl(token, hypernet):
    trips = list(zip(token, token[1:], token[2:]))
    print(trips)
    return max([(a,b,c) if a == c and a != b and b+a+b in hypernet else ('zzz', ) for (a, b, c) in trips])

n_tls = 0
n_ssl = 0

for line in lines:
    tokens = re.findall(r'[^\[\]]{1,}|\[.*?\]', line)
    if supports_tls( list(map(has_abba, tokens)) ):
        n_tls += 1

    hypernet = ''.join(tokens[1::2])
    print(hypernet)

    for token in tokens[0::2]:
        x = supports_ssl(token, hypernet)
        if x:
            print(x, hypernet, tokens)
            n_ssl += 1
            break

print(len(lines))
print(n_tls, n_ssl)
