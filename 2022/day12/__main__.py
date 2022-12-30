

def letter_to_value(char):
    return ord(char) - ord("a")


with open("./day12/input.txt", "r", encoding="utf-8") as input_file:
    elevation_map = [[letter_to_value(cell) for cell in row.strip()]
                     for row in input_file.readlines()]

map_height = len(elevation_map) - 1
map_width = len(elevation_map[0]) - 1


class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other: 'Coord'):
        return Coord(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'(x:{self.x}, y:{self.y})'

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


def ele_from_coord(coord: Coord = None, x: int = None, y: int = None):
    if not coord is None:
        x, y = coord.x, coord.y
    return elevation_map[y][x]


class PathNode:
    def __init__(self, previous: Coord, my_coord: Coord, elevation: int, distance: int) -> None:
        self.previous = previous
        self.current = my_coord
        self.elevation = elevation
        self.distance = distance

    def __str__(self) -> str:
        return f'(prev:{str(self.previous)}, curr:{str(self.current)}, elev:{self.elevation}, dist:{self.distance})'


def find_where_elevation_is(elevation):
    for pos_y in range(map_height + 1):
        for pos_x in range(map_width + 1):
            if elevation_map[pos_y][pos_x] == elevation:
                return Coord(pos_x, pos_y)
    return None


def lies_between(x, a, b):
    return x >= a and x <= b


def dequeue(stack: list) -> 'tuple[list, object]':
    element = stack[0]
    stack = stack[1:]
    return stack, element


location = find_where_elevation_is(letter_to_value("S"))
destination = find_where_elevation_is(letter_to_value("E"))
elevation_map[location.y][location.x] = letter_to_value("a")
elevation_map[destination.y][destination.x] = letter_to_value("z")


def get_neighbor(origin_coord: Coord, neighbor_direction: Coord) -> 'tuple[Coord, int]':
    origin_coord = origin_coord + neighbor_direction
    if not (lies_between(origin_coord.x, 0, map_width) and
            lies_between(origin_coord.y, 0, map_height)):
        return None, None
    elevation = elevation_map[origin_coord.y][origin_coord.x]
    return origin_coord, elevation


def solution(start_location, is_part_two, initial_letter):
    active_coords = [start_location]
    passed_neighbors = set()
    passed_neighbors.add(start_location)
    shortest_neighbor_map = {
        start_location: PathNode(None, start_location,
                                 letter_to_value(initial_letter), 0)
    }

    neighbor_mask = [Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)]
    while len(active_coords) > 0:
        active_coords, current_coord = dequeue(active_coords)
        passed_neighbors.add(current_coord)
        current_elevation = elevation_map[current_coord.y][current_coord.x]
        current_path = shortest_neighbor_map[current_coord]
        for mask in neighbor_mask:
            target_coord, target_elevation = get_neighbor(current_coord, mask)
            # skips irrelevant neighbors
            if is_part_two:
                right_elevation = target_coord is None or \
                    current_elevation - target_elevation > 1
            else:
                right_elevation = target_coord is None or \
                    target_elevation - current_elevation > 1
            if right_elevation:
                continue
            # adds unvisited neighbors
            if target_coord not in passed_neighbors \
                    and target_coord not in active_coords:
                active_coords.append(target_coord)
            # updates paths wherever necessary
            new_distance = current_path.distance + 1
            if target_coord not in shortest_neighbor_map or \
                    new_distance < shortest_neighbor_map[target_coord].distance:
                shortest_neighbor_map[target_coord] = PathNode(
                    current_coord, target_coord, target_elevation, new_distance)

    return shortest_neighbor_map


# part 1
sn_map = solution(location, False, "a")
shortest_distance = sn_map[destination].distance
print(f'{shortest_distance=}')

# part 2
sn_map = solution(destination, True, "z")
valleys = [ele for ele in sn_map.values() if ele.elevation ==
           letter_to_value("a")]
shortest = sorted(valleys, key=lambda x: x.distance)
shortest_distance = shortest[0].distance
print(f'{shortest_distance=}')
