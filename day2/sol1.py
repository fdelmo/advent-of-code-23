with open("day2/data/input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

cubes_in_bag = {"red": 12, "blue": 14, "green": 13}


valid_games = []
for line in data:
    game, sets = line.split(":")
    game_id = int(game.split(" ")[-1])

    sets = sets.split(";")

    game_valid = True
    for i in sets:
        dices = i.split(",")

        for die in dices:
            number, color = die.strip().split(" ")

            if int(number) > cubes_in_bag[color.lower()]:
                game_valid = False
                break

        if not game_valid:
            break

    if game_valid:
        valid_games.append(game_id)

print(sum(valid_games))
