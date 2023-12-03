import string

with open("day3/data/input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]


row_len = len(data[0])
rows_in_data = len(data)
for i, row in enumerate(data):
    for j, ch in enumerate(row):
        # check if correct symbol
        if ch == "*":
            # check possible surroundings without falling out of
            # bounds of the file
            if j == 0:
                h_steps = range(0, 2)
            elif j == (row_len - 1):
                h_steps = range(-1, 1)
            else:
                h_steps = range(1, 2)

            if i == 0:
                v_steps = range(0, 2)
            elif i == (rows_in_data - 1):
                v_steps = range(-1, 1)
            else:
                v_steps = range(1, 2)
