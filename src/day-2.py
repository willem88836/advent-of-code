
# Advent of Code day 2

entry_file = open("./data/day-2.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)


# Part 1

valid_key_count = 0

for i in range(0, entry_count): 
    entry = entries[i]
    spl = entry.split(' ')

    minmax = spl[0].split('-')
    key = spl[1].split(':')[0]
    code = spl[2]
    key_count = 0

    for c in range(0, len(code)): 
        if code[c] == key: 
            key_count += 1
    
    if (key_count >= int(minmax[0]) and key_count <= int(minmax[1])): 
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
