
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


def clean_pos(pos: str):
    pos = pos.strip(", | :")
    pos = pos[2:]
    return int(pos)


def build_entry(line):
    spl = line.split(" ")
    s_x = clean_pos(spl[2])
    s_y = clean_pos(spl[3])
    b_x = clean_pos(spl[8])
    b_y = clean_pos(spl[9])
    return {
        "sensor": Coord(s_x, s_y),
        "beacon": Coord(b_x, b_y)
    }


with open("./day15/input.txt", "r", encoding="utf-8") as input_file:
    data = [build_entry(line.strip()) for line in input_file.readlines()]


def man_dist(a: Coord, b: Coord) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


# create initial blocked ranges.
blocked = {}
for entry in data:
    sensor = entry['sensor']
    beacon = entry['beacon']
    distance = man_dist(sensor, beacon) - 1

    min_y = sensor.y - distance
    max_y = sensor.y + distance

    x_grow_dir = 1
    x_radius = 0

    for step, row in enumerate(range(min_y, max_y + 1)):
        x_radius += x_grow_dir
        if row == sensor.y:
            x_grow_dir = -1
        x_range = range(sensor.x - x_radius, sensor.x + x_radius)
        if row not in blocked:
            blocked[row] = []
        blocked[row].append(x_range)


def overlaps_left(range_a: range, range_b: range):
    return range_a.start < range_b.start and \
        range_a.stop >= range_b.start and \
        range_a.stop < range_b.stop


def is_overlapped_completely_by(range_a: range, range_b: range):
    return range_a.start >= range_b.start and \
        range_a.stop <= range_b.stop


def merge_range(range_a: range, range_b: range) -> range | None:
    if is_overlapped_completely_by(blocked_range, other_blocked_range):
        return range_b
    elif is_overlapped_completely_by(other_blocked_range, blocked_range):
        return range_a
    elif overlaps_left(blocked_range, other_blocked_range):
        return range(blocked_range.start, other_blocked_range.stop)
    elif overlaps_left(other_blocked_range, blocked_range):
        return range(other_blocked_range.start, blocked_range.stop)
    return None


def build_new_blocked_ranges(all_ranges: list, range_a, range_b, merged_range) -> list:
    all_ranges.remove(range_a)
    all_ranges.remove(range_b)
    all_ranges.append(merged_range)
    return all_ranges


# Clean up duplicate blocked ranges.
for row, blocked_ranges in blocked.items():
    merged_ranges = True
    while merged_ranges:
        merged_ranges = False
        for index, blocked_range in enumerate(blocked_ranges):
            for other_blocked_range in blocked_ranges[index + 1:]:
                new_range = merge_range(blocked_range, other_blocked_range)
                if not new_range is None:
                    merged_ranges = True
                    new_ranges = build_new_blocked_ranges(
                        blocked_ranges, blocked_range, other_blocked_range, new_range)
                    blocked_ranges = new_ranges
                    blocked[row] = new_ranges
                    break
            if merged_ranges:
                break

target_row = 2000000  # 2000000
blocked_ranges = blocked[target_row]
total_blocked = 0
for blocked_range in blocked_ranges:
    total_blocked += blocked_range.stop - blocked_range.start
print(f'{total_blocked=}')


# part two
min_max = Coord(0, 4000000)  # 4000000
candidates = []
for row, blocked_ranges in blocked.items():
    if row < min_max.x or row > min_max.y:
        continue
    valid_ranges = []
    for blocked_range in blocked_ranges:
        if blocked_range.stop < min_max.x or blocked_range.start > min_max.y:
            continue
        valid_ranges.append(blocked_range)
    if len(valid_ranges) > 1:
        valid_ranges.sort(key=lambda x: x.start)
        for index, blocked_range in enumerate(valid_ranges[:-1]):
            next_range = valid_ranges[index + 1]
            if next_range.start - blocked_range.stop > 1:
                candidate = Coord(blocked_range.stop + 1, row)
                candidates.append(candidate)

tuning_frequency = candidates[0].x * 4000000 + candidates[0].y
print(f'{tuning_frequency=}')
