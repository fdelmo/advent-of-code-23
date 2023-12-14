with open("day11/data/test.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

for i, row in enumerate(data):
    data[i] = list(row)

# columns
j = 0
while j < len(data[0]):
    col = [row[j] for row in data]
    if "#" not in col:
        i = 0
        while i < len(col):
            data[i].insert(j, col[i])
            i += 1
        j += 2
    else:
        j += 1

# rows
i = 0
while i < len(data):
    if "#" not in data[i]:
        data.insert(i, data[i])
        i += 2
    else:
        i += 1

for line in data:
    print(line)
