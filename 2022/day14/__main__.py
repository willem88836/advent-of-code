
class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other: 'Coord'):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Coord'):
        return Coord(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float):
        return Coord(round(self.x * other), round(self.y * other))

    def __str__(self):
        return f'(x:{self.x}, y:{self.y})'

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


def build_entry(line):
    return [Coord(*[int(dim) for dim in entry.split(",")]) for entry in line.split(" -> ")]


with open('./day14/input.txt', 'r', encoding='utf-8') as input_file:
    data = [build_entry(line.strip()) for line in input_file.readlines()]


def lerp(a: Coord, b: Coord, t: float) -> Coord:
    return a + (b - a) * t


def man_dist(a: Coord, b: Coord) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


ROCK = 3
SAND = 2

lower_bound = max([max([entry.y for entry in entries]) for entries in data])


def solution(part_two: bool):
    grid = {}

    if part_two:
        left_bound = min([min([entry.x for entry in entries])
                         for entries in data])
        right_bound = max([max([entry.x for entry in entries])
                          for entries in data])
        padding = 1000
        data.append([Coord(left_bound - padding, lower_bound + 2),
                    Coord(right_bound + padding, lower_bound + 2)])

    for entry in data:
        for index, point in enumerate(entry[:-1]):
            next_point = entry[index + 1]
            steps = man_dist(point, next_point)

            for i in range(steps):
                t = i / steps
                cell = lerp(point, next_point, t)
                grid[cell] = ROCK
        grid[next_point] = ROCK

    dir_mask = [Coord(0, 1), Coord(-1, 1), Coord(1, 1)]
    simulation_is_running = True
    while simulation_is_running:
        has_settled = False
        sand_position = Coord(500, 0)
        while not has_settled and simulation_is_running:
            has_settled = True
            for mask in dir_mask:
                target = sand_position + mask
                if target not in grid:
                    sand_position = target
                    has_settled = False
                    if not part_two and \
                            sand_position.y >= lower_bound:
                        simulation_is_running = False
                    break
        if simulation_is_running:
            grid[sand_position] = SAND
        if sand_position == Coord(500, 0):
            simulation_is_running = False
    return grid


grid = solution(False)
sand_grid = {key: value for key, value in grid.items() if value == SAND}
total_sand = len(sand_grid)
print(f'{total_sand=}')

grid = solution(True)
sand_grid = {key: value for key, value in grid.items() if value == SAND}
total_sand = len(sand_grid)
print(f'{total_sand=}')
