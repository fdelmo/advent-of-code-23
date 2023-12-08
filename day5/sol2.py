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
            numbers = [
                int(number.strip())
                for number in numbers.split(" ")
                if number.strip() != ""
            ]

            seeds_ranges = []
            range_dic = {}
            for i, num in enumerate(numbers):
                if i % 2 == 0:
                    range_dic["start"] = num
                else:
                    range_dic["range"] = num
                    seeds_ranges.append(range_dic.copy())

        continue

    map = dict(
        zip(
            ["dest_start", "src_start", "range"],
            [int(num) for num in line.strip().split(" ")],
        )
    )
    tables[table_name].append(map)


def check_if_seed_exists(seed, seed_ranges):
    """
    Check if given seed is in any of the ranges in seed_ranges.
    """
    for seed_range in seed_ranges:
        if (seed >= seed_range["start"]) and (
            seed < (seed_range["start"] + seed_range["range"])
        ):
            return True

    return False


min_loc = 0
check = min_loc

while True:
    for table in tables.__reversed__():
        for map in tables[table]:
            if (check >= map["dest_start"]) and (
                (check - map["dest_start"]) < map["range"]
            ):
                check = map["src_start"] + (check - map["dest_start"])
                break

    found_seed = check

    min_seed_exists = check_if_seed_exists(found_seed, seeds_ranges)

    if min_seed_exists:
        break

    min_loc += 1
    check = min_loc


print(f"minimum final location: {min_loc}")
