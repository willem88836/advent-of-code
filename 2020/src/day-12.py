
# Advent of Code day 12

import math

entry_file = open("./data/day-12.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)
entry_width = len(entries[0].strip())


# Part 1

x = 0
y = 0
r = 0

for i in range(0, entry_count): 
    entry = entries[i].strip()

    key = entry[0]
    dist = int(entry[1:])

    if key == 'N': 
        y += dist
    elif key == 'S': 
        y -= dist
    elif key == 'E': 
        x += dist
    elif key == 'W': 
        x -= dist
    elif key == 'F': 
        q = math.radians(r)
        x += round(math.cos(q) * dist)
        y += round(math.sin(q) * dist)
    elif key == 'L': 
        r = (r + dist) % 360
    elif key == 'R': 
        r = (r - dist) % 360

print("Distance: " + str(abs(x) + abs(y)))


# Part 2

x = 0
y = 0
w_x = 10
w_y = 1

for i in range(0, entry_count): 
    entry = entries[i].strip()

    key = entry[0]
    dist = int(entry[1:])

    if key == 'N': 
        w_y += dist
    elif key == 'S': 
        w_y -= dist
    elif key == 'E': 
        w_x += dist
    elif key == 'W': 
        w_x -= dist
    elif key == 'F': 
        x += dist * w_x
        y += dist * w_y
    elif key == 'L': 
        for k in range(0, int(dist / 90)): 
            g = -w_y
            w_y = w_x
            w_x = g 
    elif key == 'R': 
        for k in range(0, int(dist / 90)): 
            g = -w_x
            w_x = w_y
            w_y = g

print("Distance: " + str(abs(x) + abs(y)))
