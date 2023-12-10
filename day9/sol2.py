import numpy as np

with open("day9/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

forecasted_vals = []
history_vals = []
for sequence in data:
    sequence = [int(val) for val in sequence.strip().split(" ")]

    last_vals = [sequence[-1]]
    first_vals = [sequence[0]]
    while not all(val == 0 for val in sequence):
        sequence = np.diff(sequence)
        last_vals.append(sequence[-1])
        first_vals.append(sequence[0])

    forecasted_vals.append(sum(last_vals))

    val = 0
    for i in range(1, len(first_vals)):
        val = first_vals[-i - 1] - val

    history_vals.append(val)

print(f"The sum of forecatsed vals is: {sum(forecasted_vals)}")
print(f"The sum of history vals is: {sum(history_vals)}")
