with open("day4/data/input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

acc_points = []
for line in data:
    card, content = line.split(":")
    left, right = content.split("|")

    winners = [int(val) for val in left.strip().split(" ") if val != ""]
    gotten = [int(val) for val in right.strip().split(" ") if val != ""]

    exp = 0
    for val in gotten:
        if val in winners:
            exp += 1

    if exp == 0:
        continue

    points = 2 ** (exp - 1)

    acc_points.append(points)

print(sum(acc_points))
