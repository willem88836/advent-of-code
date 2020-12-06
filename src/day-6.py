
# Advent of Code day 6

entry_file = open("./data/day-6.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)


# Part 1

checked = [False] * 26
sum = 0

for i in range(0, entry_count): 
    entry = entries[i].strip()
    if len(entry) == 0: 
        checked = [False] * 26
    else: 
        for j in range(0, len(entry)): 
            e = ord(entry[j]) - 97

            if not checked[e]:
                checked[e] = True
                sum += 1

print("Total: " + str(sum))


# Part 2

checked = [0] * 26
sum = 0
people_count = 0

for i in range(0, entry_count): 
    entry = entries[i].strip()
    if len(entry) == 0: 
        for j in range(0, 26) : 
            if checked[j] == people_count: 
                sum += 1

        checked = [0] * 26
        people_count = 0
    else: 
        people_count += 1
        for j in range(0, len(entry)): 
            e = ord(entry[j]) - 97
            checked[e] += 1

print("Total: " + str(sum))
