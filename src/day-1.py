
#Advent of Code Day 1

target_sum = 2020

file1 = open("./data/day-1.dat","r")
entries = file1.readlines()
entry_count = len(entries)

for i in range(0, entry_count): 
    a = int(entries[i])
    for j in range(i, entry_count): 
        b = int(entries[j])
        if a + b == target_sum: 
            print(str(a) + " " + str(b) + " = " + str(target_sum))
            