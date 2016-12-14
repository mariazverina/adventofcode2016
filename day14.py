import hashlib

salt = "cuanljph"

# salt = "abc"

MD5_CACHE = {}
PENTUPLES = {}

def ntuple(s, n):
    tuples = zip(*[s[x:] for x in range(n)])
    same_tups = [t for t in tuples if all([c == t[0] for c in t])]
    return map(lambda x:x[0], same_tups)

def pentuples(s):
    global PENTUPLES
    if s in PENTUPLES:
        return PENTUPLES[s]
    same_tups = ntuple(s, 5)
    PENTUPLES[s] = set(same_tups)
    return same_tups

def md5(s):
    global MD5_CACHE
    if s in MD5_CACHE:
        return MD5_CACHE[s]

    d = s
    for i in range(2017):
        h = hashlib.md5()
        h.update(d)
        d = h.hexdigest()
    MD5_CACHE[s] = d
    return d

hh = md5('abc18')
print hh
print ntuple(hh, 3)
print ntuple(hh, 5)

keys = []
i = 0

while True:
    ks = ntuple(md5(salt + str(i)), 3)
    if len(ks) > 0:
        for j in range(1,1001):
            zs = pentuples(md5(salt + str(i + j)))
            if ks[0] in zs:
                keys.append((i, ks, zs))
                print keys
                break
    if len(keys) == 64:
        break

    i += 1
    # print i

print keys