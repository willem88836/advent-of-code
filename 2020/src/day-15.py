
# Advent of Code day 15

entry_file = open("./data/day-15.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)
entry_width = len(entries[0].strip())

def find_for(k): 
    starters = entries[0].strip().split(',')
    numbers = dict()

    for i in range(1, len(starters)): 
        numbers[int(starters[i - 1])] = i

    last = int(starters[len(starters) - 1])

    for j in range(i + 2, k): 
        if last in numbers: 
            next = j - 1 - numbers[last]
        else: 
            next = 0

        numbers[last] = j - 1
        last = next

    print(str(k) + "th Iteration: " + str(last))

# Part 1
find_for(2021)

# Part 2
find_for(30000001)