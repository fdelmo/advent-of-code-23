with open("day2/data/input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

powers = []
for line in data:
    game, sets = line.split(":")
    game_id = int(game.split(" ")[-1])

    sets = sets.split(";")

    min_dices = {"blue": 0, "red": 0, "green": 0}
    power = 1
    for i in sets:
        dices = i.split(",")

        for die in dices:
            number, color = die.strip().split(" ")

            if int(number) > min_dices[color.lower()]:
                min_dices[color.lower()] = int(number)

    for values in min_dices.values():
        power *= values

    powers.append(power)

print(sum(powers))
