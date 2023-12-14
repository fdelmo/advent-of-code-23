from __future__ import annotations
import pickle as pkl

with open("day11/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

for i, row in enumerate(data):
    data[i] = list(row)

class Galaxy:
    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position

    def distance_to(self, other: Galaxy) -> int:
        return abs(self.position[0] - other.position[0]) + abs(self.position[1] - other.position[1])
    

def calculate_galaxies(data: list[str], times: int =2) -> list[Galaxy]:
    # columns
    galaxies = []
    rows_empt = 0
    empy_cols_idx = []
    j = 0
    while j < len(data[0]):
        col = [row[j] for row in data]
        if "#" not in col:
            empy_cols_idx.append(j)
        j += 1

    for i,row in enumerate(data):
        if "#" not in row:
            rows_empt += 1
        
        for j, cell in enumerate(row):
            pos_y = sum([val < j for val in empy_cols_idx])
            if cell == "#":
                galaxies.append(Galaxy((i+rows_empt*(times-1), j+pos_y*(times-1))))
                
    return galaxies

galaxies = calculate_galaxies(data, times=1000000)

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