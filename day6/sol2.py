with open("day6/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

table = {}
for line in data:
    line_name, values = line.split(":")
    value = int(values.replace(" ", ""))
    table[line_name] = value


winning_possibilities = 0
for press_time in range(1, table["Time"]):
    remaining_time = table["Time"] - press_time
    dist_covered = press_time * remaining_time
    if (dist_covered < table["Distance"]) and winning_possibilities > 0:
        break

    winning_possibilities += int(dist_covered > table["Distance"])

print(winning_possibilities)
