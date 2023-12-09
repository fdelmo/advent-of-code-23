with open("day6/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

table = {}
for line in data:
    line_name, values = line.split(":")
    values = [int(value) for value in values.strip().split(" ") if value != ""]
    table[line_name] = values

races = []
for i, time in enumerate(table["Time"]):
    races.append({"time": time, "dist": table["Distance"][i]})

final_mul = 1
for race in races:
    winning_possibilities = 0
    for press_time in range(1, race["time"]):
        remaining_time = race["time"] - press_time
        dist_covered = press_time * remaining_time
        if (dist_covered < race["dist"]) and winning_possibilities > 0:
            break

        winning_possibilities += int(dist_covered > race["dist"])

    final_mul *= winning_possibilities

print(final_mul)
