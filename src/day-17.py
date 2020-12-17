
# Advent of Code day 17

import copy
import math

entry_file = open("./data/day-17.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)
entry_width = len(entries[0].strip())


# Part 1

def in_range(a, b): 
    for i in range(0, len(a)): 
        if abs(a[i] - b[i]) > 1: 
            return False
    return True

cells = []

for i in range(0, len(entries)): 
    entry = entries[i].strip()
    for j in range(0, len(entry)): 
        if entry[j] == "#": 
            cells.append([i, j, 0])

next = copy.deepcopy(cells)

for i in range(0, 1): 
    neighbour_count = dict()
    for j in range(0, 1): 
        current = cells[j]
        for x in range(-1, 2): 
            x_sh = (x + current[0]) << 32
            for y in range(-1, 2): 
                y_sh = (y + current[1] + x_sh) << 16
                for z in range(-1, 2): 
                    q = y_sh + z + current[2]
                    if q in neighbour_count: 
                        neighbour_count[q] += 1
                    else: 
                        neighbour_count[q] = 1

    print(neighbour_count.items())

    for key, value in neighbour_count.items(): 
        print("")
        print(key)
        x = key >> 32
        y = (key >> 16) - (x << 32)
        z = key - (y << 16)

        print([x,y,z])


    #     x = key >> 16
    #     y = (key - x) >> 8
    #     z = (key - y - x)
    #     print(x)
    #     print(y)
    #     print(z)

    #     print("")


