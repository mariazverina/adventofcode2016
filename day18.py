row = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."

# row = ".^^.^.^^^^"
# row = "..^^."

CELL_LOOKUP = dict(zip(['...', '..^', '.^.', '^..', '.^^', '^.^', '^^.', '^^^'], ".^.^^.^."))

n_empty = 0

for i in range(400000):
    # print(row)
    n_empty += sum([1 if x == '.' else 0 for x in row])
    row = "." + row + "."
    trips_above = (list(map(''.join, (zip(row, row[1:], row[2:])))))
    row = ''.join((map(lambda x:CELL_LOOKUP[x], trips_above)))

print(n_empty)
