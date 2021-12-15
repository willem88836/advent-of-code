
# Advent of Code day 14

import math

entry_file = open("./data/day-14.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)
entry_width = len(entries[0].strip())


# Part 1

mask = ""
memory = dict()

for i in range(0, len(entries)): 
    entry = entries[i].strip()

    if (entry[1] == 'a'): 
        split = entry.split(" ")
        mask = split[len(split) - 1]
    else: 
        split = entry.split(" ")
        location = int(split[0][4 : len(split[0]) - 1])
        value = int(split[len(split) - 1])
        binary = list(f'{value:036b}')
        
        masked_value = 0
        for j in range(0, len(binary)): 
            if mask[j] == "0":
                binary[j] = '0'
            elif mask[j] == "1":
                binary[j] = '1'
                
            masked_value += int(binary[j]) * math.pow(2, len(binary) - j - 1)

        memory[location] = masked_value

sum = 0
for key, value in memory.items(): 
    sum += value

print("Sum: " + str(int(sum)))


# Part 2

mask = ""
float_count = 0
memory = dict()

for i in range(0, len(entries)): 
    entry = entries[i].strip()

    if (entry[1] == 'a'): 
        split = entry.split(" ")
        mask = split[len(split) - 1]
        float_count = 0
        for j in range(0, len(mask)): 
            if mask[j] == "X": 
                float_count += 1
    else: 
        split = entry.split(" ")
        location = int(split[0][4 : len(split[0]) - 1])
        binary = list(f'{location:036b}')
        value = int(split[len(split) - 1])

        for j in range(0, len(binary)): 
            if mask[j] == "X":
                binary[j] = 'X'
            elif mask[j] == "1":
                binary[j] = '1'

        for j in range(0, int(math.pow(2, float_count)) + 1): 
            floats = list(f'{j:036b}')
            f = 0
            location = 0
            
            for k in range(0, len(binary)):
                masked_bit = binary[k]
                if masked_bit == "X": 
                    masked_bit = floats[len(floats) - f - 1]
                    f += 1
                location += int(masked_bit) * math.pow(2, len(binary) - k - 1)

            memory[location] = value
            
sum = 0
for key, value in memory.items(): 
    sum += value

print("Sum: " + str(int(sum)))
