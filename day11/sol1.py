from __future__ import annotations

with open("day11/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

for i, row in enumerate(data):
    data[i] = list(row)

class Galaxy:
    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position

    def distance_to(self, other: Galaxy) -> int:
        return abs(self.position[0] - other.position[0]) + abs(self.position[1] - other.position[1])

def expand_universe(data: list[str]) -> list[str]:
    # columns
    j = 0
    while j < len(data[0]):
        col = [row[j] for row in data]
        if "#" not in col:
            i = 0
            while i < len(col):
                data[i].insert(j, col[i])
                i += 1
            j += 2
        else:
            j += 1

    # rows
    i = 0
    while i < len(data):
        if "#" not in data[i]:
            data.insert(i, data[i])
            i += 2
        else:
            i += 1
    
    return data



data = expand_universe(data)

galaxies= []
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell == "#":
            galaxies.append(Galaxy((i, j)))

# find distance of each galaxy with each other only once
distances = {}
for galaxy in galaxies:
    for other in galaxies:
        if galaxy == other:
            continue
        pair = galaxy.position, other.position
        if pair in distances:
            continue
        rev_pair = other.position, galaxy.position
        distances[rev_pair] = galaxy.distance_to(other)
        

total_dist = 0
for pair, distance in distances.items():
    total_dist += distance

print(total_dist)