with open("day5/data/input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]


tables = {}
for line in data:
    if line == "":
        continue

    if ":" in line:
        table_name = line.split(":")[0]
        if table_name != "seeds":
            tables[table_name] = []

        elif table_name == "seeds":
            numbers = line.split(":")[-1]
            seeds = [
                int(number.strip())
                for number in numbers.split(" ")
                if number.strip() != ""
            ]

        continue

    map = dict(
        zip(
            ["dest_start", "src_start", "range"],
            [int(num) for num in line.strip().split(" ")],
        )
    )
    tables[table_name].append(map)

# find the location per seed

final_locations = []
# iteration per seed
for seed in seeds:
    check = seed  # we start checking the value of the seed
    # iteration per table
    for table, mappings in tables.items():
        # iteration per line
        for map in mappings:
            if (check >= map["src_start"]) and (
                (check - map["src_start"]) < map["range"]
            ):
                check = map["dest_start"] + (check - map["src_start"])
                break

        if table != "humidity-to-location map":
            continue

        final_locations.append(check)

print(min(final_locations))
