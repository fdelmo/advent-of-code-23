from collections import deque

with open("day4/data/input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

copies = deque([0])
total_cards = 0
for line in data:
    card, content = line.split(":")
    left, right = content.split("|")

    winners = [int(val) for val in left.strip().split(" ") if val != ""]
    gotten = [int(val) for val in right.strip().split(" ") if val != ""]

    # cards of this number including the copies:
    try:
        equal_cards = 1 + copies.popleft()
    except IndexError:
        equal_cards = 1

    total_cards += equal_cards

    copies_won = 0
    for val in gotten:
        if val in winners:
            copies_won += 1

    for i in range(copies_won):
        try:
            copies[i] += equal_cards
        except IndexError:
            copies.append(equal_cards)

print(total_cards)
