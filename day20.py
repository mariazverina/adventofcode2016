with open(__file__[:-2]+"txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

lines = sorted([tuple(map(int, pair.split('-'))) for pair in lines])


print(len(lines))
def dedup(intervals):
    if len(intervals) < 2:
        return intervals

    head = intervals.pop(0)

    while len(intervals) > 0 and head[1] + 1 >= intervals[0][0] :  #overlapping
        second = intervals.pop(0)
        merged = (head[0], max(head[1], second[1]))
        head = merged

    return [head] + dedup(intervals)

# print(lines)
lines = dedup(lines)

print("first = ", lines[0][1] + 1)

black_list_len = sum([b - a + 1 for a,b in lines])

print("whitelist = ", 4294967296 - black_list_len)