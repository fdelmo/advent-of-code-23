with open("day8/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

sequence = data.pop(0)

nodes = {}
for line in data:
    if line == "":
        continue
    node, directions = line.replace(")", "").replace("(", "").split("=")
    node = node.strip()
    directions = directions.replace(" ", "").split(",")

    directions = dict(zip(["L", "R"], directions))
    nodes[node] = directions

node = "AAA"
i = 0
steps = 0
while node != "ZZZ":
    order = sequence[i]
    node = nodes[node][order]
    i = (i + 1) % len(sequence)
    steps += 1

print(steps)
