
# Advent of Code day 9
import sys

entry_file = open("./data/day-9.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)


# Part 1

q = 25

for i in range(q + 1, entry_count): 
    a = int(entries[i])
    valid = False
    for j in range(i - q, i): 
        b = int(entries[j])
        for k in range(j + 1, i): 
            c = int(entries[k])
            if (c + b == a): 
                valid = True
                break 
        if valid: 
            break
    if not valid: 
        break

invalid_entry = int(entries[i])
print("Invalid Entry: " + str(i) + " - " + str(invalid_entry))


# Part 2

for length in range(2, 50):
    sum = 0 
    subset = entries[0 : length]
    
    for i in range(0, len(subset)): 
        sum += int(subset[i])

    for i in range(length, entry_count): 
        if sum == invalid_entry: 
            break

        sum += int(entries[i])
        sum -= int(entries[i - length])

    if sum == invalid_entry:
        break

subset = entries[i - length : i]

min = sys.maxsize
max = 0
for i in range(0, len(subset)): 
    a = int(subset[i]) 
    if a < min: 
        min = a
    if a > max:
        max = a

sum = min + max

print("MinMax Sum: " + str(sum))
