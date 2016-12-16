import operator

def dragon(x):
    return x + [False] + map(operator.not_, input)[::-1]

def decode(x):
    return ''.join(map(lambda q:str(int(q)), x))

input = "00101000101111010"
input = map(lambda x:x=='1', input)

req_len = 35651584

while len(input) < req_len:
    input = dragon(input)
    print len(input)
    # print decode(input)

input = input[:req_len]

while len(input) % 2 == 0:
    input = [a == b for a,b in zip(*([iter(input)]*2))]
    print len(input)

print decode(input)