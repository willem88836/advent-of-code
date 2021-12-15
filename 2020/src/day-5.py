
# Advent of Code day 4
import math

entry_file = open("./data/day-5.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)


# Part 1 & 2

def binsearch(width, key, key_high, key_low): 
    low = 0
    high = width - 1

    key_lenght = len(key)

    for j in range(0, key_lenght): 
        k = key[j]
        e =  key_lenght - (1 + j)
        shift = math.pow(2, e)
        if (k == key_high): 
            low += shift
        elif (k == key_low): 
            high -= shift

    return int(high)

n = 862
taken_seats = [False] * n

highest_id = 0
for i in range(0, entry_count):
    ticket = entries[i].strip()
    seat_row = binsearch(128, ticket[0:7], 'B', 'F')
    seat_col = binsearch(8, ticket[7:11], 'R', 'L')
    seat_id = seat_row * 8 + seat_col
    if seat_id > highest_id: 
        highest_id = seat_id
    taken_seats[int(seat_id)] = True

print("Highest seat id: " + str(highest_id))

searching = False
my_seat = 0
for i in range(0, n):
    if (taken_seats[i] and not searching): 
        searching = True
        continue
    
    if not taken_seats[i] and searching: 
        my_seat = i
        break

print("My seat: " + str(my_seat))
