with open("day11/data/test.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

# rows
i = 0
while i < len(data):
    data[i] = list(data[i])
    if "#" not in data[i]:
        data.insert(i, data[i])
        i += 2
    else:
        i += 1

# columns
j = 0
while j < len(data[0]):
    col = [row[j] for row in data]
    if "#" not in col:
        i = 0
        while i < len(col):
            data[i].insert(j, col[i])  # this wrong
            i += 1
        j += 2
    else:
        j += 1

for line in data:
    print(line)
