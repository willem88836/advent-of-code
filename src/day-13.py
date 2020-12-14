
# Advent of Code day 12

import math

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

# bus_arrival = []

# for i in range(0, len(busses)): 
#     entry = busses[i]
#     if (entry != "x"): 
#         bus_arrival.append([int(entry), i])

# print(str(bus_arrival))

# def my_func(a_k, a_r, b_i): 
#     global bus_arrival
#     b_k = bus_arrival[b_i][0]
#     b_r = bus_arrival[b_i][1]
#     lcm = a_k * b_k

#     print(str(range(a_k + a_r, lcm, a_k)))

#     for i in range(a_k + a_r, lcm, a_k): 
#         if i % b_k == b_r: 
#             print(i)
#             if b_i == len(bus_arrival) - 1: 
#                 return i
#             else:
#                 return my_func(i, 0, b_i + 1)
    
#     print("idk what happened.")

# q = my_func(bus_arrival[0][0], bus_arrival[0][1], 1)

# print(q)






# a = 1
# b = 0
# for i in range(0, len(bus_arrival)): 
#     x = bus_arrival[i][0]
#     y = bus_arrival[i][1]

#     a = a * x 
#     b = a * y + b 

#     print(str(i) + "]: " + str(a) + ", " + str(b))

# print(str(a + b))


# print(str(bus_arrival))





# g = 1.0
# for p in range(0, len(bus_arrival)): 
#     g *= bus_arrival[p][0]

# for i in range(0, len(bus_arrival)): 
#     print(str(g % bus_arrival[i][0]))




# for i in range(1, 10000000): 
#     k = i * g
#     is_sequence = True
#     for j in range(0, len(bus_arrival)): 
#         if k % bus_arrival[j][0] != bus_arrival[j][1]: 
#             is_sequence = False
#             break
#     if is_sequence: 
#         break
# print ("k: " + str(k))
# print("i: " + str(i))




# print("g: " + str(g))
# x = 0.0
# for k in range(0, len(bus_arrival)): 
#     m = bus_arrival[k][0]
#     a = bus_arrival[k][1]

#     b = g / m
#     c = (1 / b) % m
#     x += (a * b * c) % g

#     print("m: " + str(m) + ", a: " + str(a) + ", b: " + str(b) + ", c: " + str(c))

# print("x: " + str(x))

# for k in range(0, len(bus_arrival)): 
#     q = x % bus_arrival[k][0]
#     print(str(q))

