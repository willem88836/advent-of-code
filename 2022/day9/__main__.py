import numpy as np


def build_entry(line):
    spl = line.split(" ")
    return {
        "dir": spl[0],
        "count": int(spl[1])
    }


class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f'x:{self.x}, y:{self.y}'

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)


def x_dist(coord_a, coord_b):
    return abs(coord_a.x - coord_b.x)


def y_dist(coord_a, coord_b):
    return abs(coord_a.y - coord_b.y)


with open("./day9/input.txt", "r", encoding='utf-8') as input_file:
    data = [build_entry(line.strip()) for line in input_file.readlines()]

head_coord = Coord()
knot_coord = Coord()

knot_positions = set()
knot_positions.add(knot_coord)

for entry in data:
    for _ in range(entry['count']):
        # update head
        match entry['dir']:
            case 'L':
                head_coord.x -= 1
            case 'R':
                head_coord.x += 1
            case 'D':
                head_coord.y -= 1
            case 'U':
                head_coord.y += 1

        # update knot
        new_knot_coord = Coord(knot_coord.x, knot_coord.y)
        xdist = x_dist(head_coord, knot_coord)
        ydist = y_dist(head_coord, knot_coord)
        move_diag = xdist > 0 and ydist > 0 and max(xdist, ydist) > 1
        if move_diag or xdist > 1:
            new_knot_coord.x += np.sign(head_coord.x - knot_coord.x)
        if move_diag or ydist > 1:
            new_knot_coord.y += np.sign(head_coord.y - knot_coord.y)
        knot_coord = new_knot_coord
        knot_positions.add(new_knot_coord)

print(f'{len(knot_positions)=}')

# PART 2
head_coord = Coord()
tails = [Coord() for _ in range(9)]
knot_positions = set()

for entry in data:
    for _ in range(entry['count']):
        # update head
        match entry['dir']:
            case 'L':
                head_coord.x -= 1
            case 'R':
                head_coord.x += 1
            case 'D':
                head_coord.y -= 1
            case 'U':
                head_coord.y += 1

        for index, knot_coord in enumerate(tails):
            target_coord = tails[index - 1] if index > 0 else head_coord
            # update knot
            new_knot_coord = Coord(knot_coord.x, knot_coord.y)
            xdist = x_dist(target_coord, knot_coord)
            ydist = y_dist(target_coord, knot_coord)
            move_diag = xdist > 0 and ydist > 0 and max(xdist, ydist) > 1
            if move_diag or xdist > 1:
                new_knot_coord.x += np.sign(target_coord.x - knot_coord.x)
            if move_diag or ydist > 1:
                new_knot_coord.y += np.sign(target_coord.y - knot_coord.y)
            tails[index] = new_knot_coord
            if index == len(tails) - 1:
                knot_positions.add(new_knot_coord)

print(f'{len(knot_positions)=}')
