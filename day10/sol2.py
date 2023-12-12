from enum import Enum
import copy

with open("day10/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]


class Direction(Enum):
    UP = -1
    DOWN = 1
    RIGHT = 2
    LEFT = -2

    def __invert__(self):
        opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.RIGHT: Direction.LEFT,
            Direction.LEFT: Direction.RIGHT,
        }
        return opposite_directions[self]


class Pipe:
    """
    Base class of a pipe.
    """

    def __init__(self, type: str, position: tuple[int], is_part_of_loop:bool = False) -> None:
        self.directions = ()

        self.type = type
        self.position = position
        self.is_start_pipe = type == "S"

        self.is_part_of_loop = is_part_of_loop

        if self.type == "-":
            self.directions = (Direction.LEFT, Direction.RIGHT)
        elif self.type == "|":
            self.directions = (Direction.UP, Direction.DOWN)
        elif self.type == "L":
            self.directions = (Direction.UP, Direction.RIGHT)
        elif self.type == "7":
            self.directions = (Direction.LEFT, Direction.DOWN)
        elif self.type == "F":
            self.directions = (Direction.RIGHT, Direction.DOWN)
        elif self.type == "J":
            self.directions = (Direction.LEFT, Direction.UP)
        elif self.type == "S":
            self.directions = (
                Direction.UP,
                Direction.DOWN,
                Direction.LEFT,
                Direction.RIGHT,
            )
        elif self.type != ".":
            raise TypeError(f"Pipe type not valid. Type passed: {type}")

    def __str__(self) -> str:
            return f"Pipe{self.type, self.position}, is_part_of_loop: {self.is_part_of_loop}"

    def copy(self):
        return copy.deepcopy(self)

    def _next_position(self, dir: Direction) -> tuple[int]:
        if dir in (Direction.UP, Direction.DOWN):
            return self.position[0] + dir.value, self.position[1]

        return self.position[0], self.position[1] + int(dir.value / 2)

    def move(self, from_side: Direction) -> tuple[Direction, tuple[int]]:
        """
        Given a side entering the pipe, return the direction of exit and what
        position in the map that corresponds to.
        """
        if from_side not in self.directions:
            raise ValueError(f"The tile has no connection from {from_side}.")

        if self.type == "S":
            return ~from_side, self._next_position(~from_side)

        for dir in self.directions:
            if dir != from_side:
                return dir, self._next_position(dir)


def look_for_initial_directions(
    starting_pipe: Pipe, map: list[list[Direction]]
) -> list[Direction]:
    """
    Look for the directions in which the initial pipe has valid connections.
    """
    val_dirs = []
    for dir in Direction:
        dir, test_position = starting_pipe.move(dir)
        if ~dir in map[test_position[0]][test_position[1]].directions:
            val_dirs.append(dir)

    return val_dirs


# construct a map of pipes not strings
map = []
for i, line in enumerate(data):
    map_line = []
    for j, ch in enumerate(line):
        if ch == "S":
            starting_pos = i, j
        map_line.append(Pipe(type=ch, position=(i, j)))
    map.append(map_line)

tile_a = map[starting_pos[0]][starting_pos[1]]
tile_a.is_part_of_loop = True
tile_b = tile_a.copy()
position_a = tile_a.position
direction_a, direction_b = look_for_initial_directions(tile_a, map)
steps = 0
while True:
    prev_position_a = position_a
    direction_a, position_a = tile_a.move(~direction_a)
    tile_a = map[position_a[0]][position_a[1]]
    tile_a.is_part_of_loop = True

    direction_b, position_b = tile_b.move(~direction_b)
    tile_b = map[position_b[0]][position_b[1]]
    tile_b.is_part_of_loop = True

    steps += 1
    if (position_a == position_b) or (prev_position_a == position_b):
        break

# count enclosed tiles algorithm
enclosed_tiles = 0
for row in map:
    count_tile = False
    vertical_dirs = []
    for tile in row:
        if not tile.is_part_of_loop:
            if count_tile:
                enclosed_tiles += 1
            continue

        if tile.type == "S":
            tile = tile.copy()
            tile.directions = look_for_initial_directions(tile,map)

        if Direction.UP in tile.directions:
            if Direction.UP in vertical_dirs:
                vertical_dirs.remove(Direction.UP)
            else:
                vertical_dirs.append(Direction.UP)

        if Direction.DOWN in tile.directions:
            if Direction.DOWN in vertical_dirs:
                vertical_dirs.remove(Direction.DOWN)
            else:
              vertical_dirs.append(Direction.DOWN)
        
        if len(vertical_dirs) == 2:
            count_tile = not count_tile
            vertical_dirs = []

print(enclosed_tiles)