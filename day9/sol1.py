import numpy as np

with open("day9/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

forecasted_vals = []
for sequence in data:
    sequence = [int(val) for val in sequence.strip().split(" ")]

    last_vals = [sequence[-1]]
    while not all(val == 0 for val in sequence):
        sequence = np.diff(sequence)
        last_vals.append(sequence[-1])

    forecasted_vals.append(sum(last_vals))

print(sum(forecasted_vals))
