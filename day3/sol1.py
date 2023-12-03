import string

with open("day3/data/input1.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

row_len = len(data[0])
rows_in_data = len(data)
ch_not_symbols = string.digits + "."

valid_numbers = []
for i, row in enumerate(data):
    number = ""
    is_valid_number = False
    for j, ch in enumerate(row):
        if ch.isdigit():
            number += ch

            # if we already checked that the number is valid we don't
            # need to continue checking. Just finish looking for al the
            # digits in the number
            if is_valid_number:
                if j == (row_len - 1):
                    valid_numbers.append(int(number))
                continue

            # check right (first check that there are more character
            # and then checking those)
            if j < (row_len - 1):
                is_valid_number = row[j + 1] not in ch_not_symbols

                if is_valid_number:
                    continue

            if j != 0:
                is_valid_number = row[j - 1] not in ch_not_symbols

                if is_valid_number:
                    continue

            if j == (row_len - 1):
                steps = range(-1, 1, 1)
            elif j == 0:
                steps = range(0, 2, 1)
            else:
                steps = range(-1, 2, 1)

            # up (straight and diagonally)
            if i != 0:
                ch_up = [data[i - 1][j + step] for step in steps]
                is_valid_number = any(ch not in ch_not_symbols for ch in ch_up)

                if is_valid_number:
                    continue

            # down (straight and diagonally)
            if i != (rows_in_data - 1):
                ch_down = [data[i + 1][j + step] for step in steps]
                is_valid_number = any(ch not in ch_not_symbols for ch in ch_down)

                if is_valid_number:
                    continue

        elif is_valid_number:
            valid_numbers.append(int(number))
            number = ""
            is_valid_number = False

        else:
            number = ""
            is_valid_number = False

print(sum(valid_numbers))
