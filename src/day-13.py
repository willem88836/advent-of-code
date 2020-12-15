
# Advent of Code day 12

import math
import threading

entry_file = open("./data/day-13.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)


# Part 1

arrival = int(entries[0])

best_line = -1
line_wait_time = 99999

busses = entries[1].strip().split(",")
for i in range(0, len(busses)): 
    entry = busses[i]
    if entry == "x": 
        continue
    line = int(entry)

    q = math.ceil(arrival / float(line)) * line
    d = q - arrival

    if d < line_wait_time: 
        line_wait_time = d
        best_line = line

print("Best Line times delay: " + str(best_line * line_wait_time))



# Part 2

class pathFinder(threading.Thread): 
    i = 0
    k = 0
    busses = None

    def __init__(self, i, k, busses): 
        threading.Thread.__init__(self)
        self.i = i 
        self.k = k
        self.busses = busses
        print("thread (" + str(i) + ", " + str(k) + ") started")

    def run(self): 
        j = i

        searching = True

        while searching: 
            j += k
            
            valid = True

            for l in range(0, len(self.busses)): 
                entry = self.busses[l]
                d = entry[0]    
                r = entry[1]

                if (j + r) % d != 0: 
                    valid = False
                    break
            if valid: 
                searching = False
        
        print(j)




bus_arrival = []

for i in range(0, len(busses)): 
    entry = busses[i]
    if (entry != "x"): 
        bus_arrival.append([int(entry), i])


k = 8
for i in range(0, k): 
    finder = pathFinder(i, k, bus_arrival)
    finder.start()

