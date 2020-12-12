
# Advent of Code day 10

entry_file = open("./data/day-10.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)


# Part 1

sorted_list = [-1] * entry_count

for i in range(0, entry_count):
    entry = int(entries[i].strip())
    
    for j in range(0, entry_count): 
        sorted_entry = sorted_list[j]
        if sorted_entry == -1 or entry < sorted_entry: 
            sorted_list[j] = entry
            for k in range(j + 1, entry_count): 
                if sorted_entry == -1: 
                    break

                entry = sorted_list[k]
                sorted_list[k] = sorted_entry
                sorted_entry = entry
            break
            
intervals = [0] * 10
intervals[1] = 1
intervals[3] = 1
for i in range(0, entry_count - 1): 
    delta = sorted_list[i + 1] - sorted_list[i]
    intervals[delta] += 1

print("Difference Product: " + str(intervals[1] * intervals[3]))


# Part 2

joltage_range = 3

entry_count = (entry_count + 2)
entry_list = [0] * entry_count
for i in range(0, len(sorted_list)): 
    entry_list[i + 1] = sorted_list[i]
entry_list[len(entry_list) - 1] = sorted_list[len(sorted_list) - 1] + joltage_range

options = [0] * entry_count
options[entry_count - 1] = 1

for i in range(entry_count - 1, -1, -1): 
    current = int(entry_list[i])
    current_options = options[i]
    for j in range(i + 1, entry_count): 
        succeeding = entry_list[j]
        delta = succeeding - current
        if delta > joltage_range: 
            break
        current_options += options[j]

    options[i] = current_options

print("Number of Options: " + str(options[0]))
