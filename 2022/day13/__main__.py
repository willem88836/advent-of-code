import numpy as np
import functools


def try_parse_int(string: str) -> int:
    try:
        return True, int(string)
    except:
        return False, None


def create_list(line):
    if not line.startswith("["):
        return int(line)
    line = line[1:-1]
    splits = [0]
    bracket_depth = 0
    for index, char in enumerate(line):
        match char:
            case "[":
                bracket_depth += 1
            case "]":
                bracket_depth -= 1
            case ",":
                if bracket_depth == 0:
                    splits.append(index)
            case _:
                pass
    splits.append(len(line))
    sub_lists = []
    for index, (start, end) in enumerate(zip(splits[0:-1], splits[1:])):
        substring = line[start: end]
        if index > 0:
            substring = substring[1:]
        if len(substring) == 0:
            continue
        sub_list = create_list(substring)
        sub_lists.append(sub_list)
    return sub_lists


def create_entry(lines):
    lines = [line.strip() for line in lines]
    return {
        "left": create_list(lines[0]),
        "right": create_list(lines[1])
    }


with open("./day13/input.txt", "r", encoding="utf-8") as input_file:
    data = input_file.readlines()
    stride = 3
    entries = [create_entry(data[index: index + stride - 1])
               for index in range(0, len(data), stride)]


def are_right_order(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return np.sign(right - left)
    elif isinstance(left, int) and not isinstance(right, int):
        return are_right_order([left], right)
    elif not isinstance(left, int) and isinstance(right, int):
        return are_right_order(left, [right])
    for inner_left, inner_right in zip(left, right):
        the_order = are_right_order(inner_left, inner_right)
        if the_order < 0:
            return -1
        if the_order > 0:
            return 1
    if len(left) == len(right):
        return 0
    elif len(left) < len(right):
        return 1
    else:
        return -1


summed_indices = 0
for index, entry in enumerate(entries, start=1):
    order = are_right_order(entry['left'], entry['right'])
    if order >= 0:
        summed_indices += index

print(f'{summed_indices=}')

# part 2
all_packets = [[[2]], [[6]]]
for entry in entries:
    all_packets.append(entry['left'])
    all_packets.append(entry['right'])
all_packets.sort(key=functools.cmp_to_key(are_right_order), reverse=True)

index_prod = 1
for index, packet in enumerate(all_packets, start=1):
    if isinstance(packet, list) and len(packet) == 1 and \
        isinstance(packet[0], list) and len(packet[0]) == 1 and \
        isinstance(packet[0][0], int) and \
            (packet[0][0] == 2 or packet[0][0] == 6):
        index_prod *= index
print(f'{index_prod=}')
