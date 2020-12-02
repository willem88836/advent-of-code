
# Advent of Code day 2

file1 = open("./data/day-2.dat","r")
entries = file1.readlines()
entry_count = len(entries)


# Part 1

valid_key_count = 0

for i in range(0, entry_count): 
    entry = entries[i]
    spl = entry.split(' ')

    minmax = spl[0].split('-')
    key = spl[1].split(':')[0]
    code = spl[2]
    keycount = 0

    for c in range(0, len(code)): 
        if code[c] == key: 
            keycount += 1
    
    if (keycount >= int(minmax[0]) and keycount <= int(minmax[1])): 
        valid_key_count += 1

print("Number of valid keys: " + str(valid_key_count))


# Part 2

valid_key_count = 0

for i in range(0, entry_count): 
    entry = entries[i]
    spl = entry.split(' ')

    indices = spl[0].split('-')
    key = spl[1].split(':')[0]
    code = spl[2]

    a = code[int(indices[0]) - 1]
    b = code[int(indices[1]) - 1]

    if ((a == key) ^ (b == key)) == True: 
        valid_key_count += 1

print("Number of valid keys: " + str(valid_key_count))
