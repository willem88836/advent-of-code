
#Advent of Code Day 1

target_sum = 2020

file1 = open("./data/day-1.dat","r")
entries = file1.readlines()
entry_count = len(entries)

# part 1

for i in range(0, entry_count): 
    a = int(entries[i])
    for j in range(i, entry_count): 
        b = int(entries[j])
        if a + b == target_sum: 
            prod = a * b
            print(str(a) + " * " + str(b) + " = " + str(prod))
            

# part 2

for i in range(0, entry_count): 
    a = int(entries[i])
    for j in range(i, entry_count): 
        b = int(entries[j])
        for k in range(j, entry_count):
            c = int(entries[k])
            if (a + b + c) == target_sum: 
                prod = a * b * c
                print(str(a) + " * " + str(b) + " * " + str(c) + " = " + str(prod))