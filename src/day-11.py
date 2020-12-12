
# Advent of Code day 11

import copy

entry_file = open("./data/day-11.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)
entry_width = len(entries[0].strip())

seat_map = [[0] * entry_width for i in range(entry_count)]
next_iteration = [[0] * entry_width for i in range(entry_count)]

seat_free = 0
seat_taken = 1
floor = -1

def createSeatMap(): 
    global seat_map, next_iteration
    for i in range(0, entry_count): 
        for j in range(0, entry_width): 
            entry = entries[i][j]
            if entry == "L": 
                next_iteration[i][j] = seat_map[i][j] = 0
            else: 
                next_iteration[i][j] = seat_map[i][j] = -1

createSeatMap()

# Part 1
is_updated = True
iterations = 0
occupied_seats = 0

while is_updated:
    is_updated = False
    iterations += 1
    for j in range(0, entry_count): 
        for k in range(0, entry_width): 
            if seat_map[j][k] == floor: 
                continue

            neighbour_count = 0

            for l in range(-1, 2): 
                p = k + l
                if p < 0 or p >= entry_width: 
                    continue
                for m in range(-1, 2): 
                    o = j + m

                    if o < 0 or o >= entry_count or l == m == 0: 
                        continue
                    if seat_map[o][p] == seat_taken: 
                        neighbour_count += 1

            if seat_map[j][k] == seat_free and neighbour_count == 0: 
                next_iteration[j][k] = seat_taken
                occupied_seats += 1
                is_updated = True
            elif seat_map[j][k] == seat_taken and neighbour_count >= 4: 
                next_iteration[j][k] = seat_free
                occupied_seats -= 1
                is_updated = True

    seat_map = copy.deepcopy(next_iteration)

print("Occupied Seats: " + str(occupied_seats))


# Part 2

is_updated = True
iterations = 0
occupied_seats = 0
createSeatMap()

while is_updated:
    is_updated = False
    iterations += 1
    for j in range(0, entry_count): 
        for k in range(0, entry_width): 
            if seat_map[j][k] == floor: 
                continue

            neighbour_count = 0
            
            r = 0
            directions  = 8
            checked_count = 0
            checked = [False] * (directions + 1)
            while checked_count < directions: 
                r += 1
                for l in range(-1, 2): 
                    for m in range(-1, 2): 
                        q = (l + 1) * 3 + m + 1
                        if checked[q] or l == m == 0: 
                            continue

                        p = l * r + k
                        o = m * r + j

                        if o < 0 or o >= entry_count or p < 0 or p >= entry_width: 
                            checked[q] = True
                            checked_count += 1
                            continue
                        tile = seat_map[o][p]
                        if tile != floor:
                            checked[q] = True
                            checked_count += 1
                            if tile == seat_taken: 
                                neighbour_count += 1
                
            if seat_map[j][k] == seat_free and neighbour_count == 0: 
                next_iteration[j][k] = seat_taken
                occupied_seats += 1
                is_updated = True
            elif seat_map[j][k] == seat_taken and neighbour_count >= 5: 
                next_iteration[j][k] = seat_free
                occupied_seats -= 1
                is_updated = True

    seat_map = copy.deepcopy(next_iteration)

print("Occupied Seats: " + str(occupied_seats))
