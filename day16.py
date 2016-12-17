import operator

def dragon(x):
    return x + [False] + [*list(map(operator.not_, input))][::-1]

def decode(x):
    return ''.join([str(int(q)) for q in x])

input = "00101000101111010"
input = [*[x=='1' for x in list(input)]]

req_len = 35651584

print(input)

while len(input) < req_len:
    input = dragon(input)
    print((len(input)))
    # print decode(input)

input = input[:req_len]

while len(input) % 2 == 0:
    input = [a == b for a,b in zip(*([iter(input)]*2))]
    print((len(input)))

print((decode(input)))