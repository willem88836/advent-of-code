
# Advent of Code day 16

entry_file = open("./data/day-16.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)
entry_width = len(entries[0].strip())


# Part 1 & 2

preamble_length = 0
near_ticket_start = 0
my_ticket = ""

for i in range(0, len(entries)):
    entry = entries[i]
    if entry == '\n': 
        if preamble_length == 0: 
            preamble_length = i
            my_ticket = entries[i + 2]
        else: 
            near_ticket_start = i + 2

entries.append(my_ticket)
rules = [[[0] * 2 for i in range(2)] for i in range(preamble_length)]
valid_ranges = [False] * 1000

for i in range(0, preamble_length): 
    ranges = entries[i].strip().split(": ")[1].split(" or ")
    for j in range(0, len(ranges)): 
        r = ranges[j]
        minmax = r.split("-")
        mn = int(minmax[0])
        mx = int(minmax[1])
        rules[i][j][:] = [mn, mx]
        valid_ranges[mn : mx] = [True] * (mx - mn)

error_rate = 0
rule_adherance = [[True] * len(rules) for i in range(len(rules))]

for i in range(near_ticket_start, entry_count + 1): 
    values = entries[i].strip().split(",")
    is_valid = True
    for v in values:
        w = int(v)
        if not valid_ranges[w]: 
            error_rate += w
            is_valid = False
    if is_valid:
        for j in range(0, len(values)):
            v = int(values[j])
            for k in range(0, len(rules)):
                if not rule_adherance[j][k]: 
                    continue
                limits = rules[k]
                is_valid = False
                for l in range(0, len(limits)): 
                    lim = limits[l]
                    if v >= lim[0] and v <= lim[1]: 
                        is_valid = True
                        break
                if not is_valid: 
                    rule_adherance[j][k] = False

print("Error rate: " + str(error_rate))


used_node_count = 0
used_nodes = [False] * preamble_length

def find_meaning(i): 
    global used_nodes
    global used_node_count

    if used_node_count >= preamble_length: 
        return [i]
    
    for w in range(0, preamble_length): 
        if used_nodes[w] or not rule_adherance[i][w]: 
            continue
        used_nodes[w] = True
        used_node_count += 1
        found = find_meaning(w)
        used_nodes[w] = False
        used_node_count -= 1
        if found != -1: 
            found.append(i)
            return found

    return -1

for i in range(0, preamble_length): 
    if i == 14: 
        continue
    print("\ni: " + str(i))
    used_node_count = 1
    used_nodes[i] = True
    found = find_meaning(i)
    used_nodes[i] = False
    # found = found[0 : len(found) - 1]
    print(str(found).replace(",", ",\t"))

