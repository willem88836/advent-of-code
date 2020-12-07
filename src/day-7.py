
# Advent of Code day 6

entry_file = open("./data/day-7.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)

search_key = "shiny gold bags"
bag_table = dict()
for i in range(0, entry_count): 
    entry = entries[i].strip()
    a = entry.split(" contain ")

    name = a[0]
    bag_table[name] = dict()

    if a[1] != "no other bags.": 
        contents = a[1].strip(".").split(", ")

        for j in range(0, len(contents)): 
            current = contents[j].strip()

            inner_bag_count = int(current[0])
            inner_bag_name = str(current[2:])

            if not inner_bag_name.endswith("s"): 
                inner_bag_name = inner_bag_name + "s"

            bag_table[name][inner_bag_name] = inner_bag_count


# Part 1

def findBag(search_key, flags, current_key):
    inner_bags = bag_table[current_key]
        
    if flags[current_key] == 0:
        if len(inner_bags) > 0:
            for bag_key, value in inner_bags.items():
                if findBag(search_key, flags, bag_key) == 1:
                    flags[current_key] = 1
                    break
            if flags[current_key] == 0: 
                flags[current_key] = -1
        else: 
            flags[current_key] = -1

    if (search_key == current_key): 
        return 1
    else: 
        return flags[current_key]
    

flags = dict()
for key, value in bag_table.items():
    flags[key] = 0

for key, value in bag_table.items():
    if flags[key] == 0:
        findBag(search_key, flags, key); 

count = 0
for key, value in flags.items():
    if value == 1: 
        count += 1

print("Total: " + str(count))



# Part 2

def innerBagCount(key): 
    inner_bags = bag_table[key]
    inner_bag_count = len(inner_bags); 

    count = 0
    if inner_bag_count > 0: 
        for key, value in inner_bags.items(): 
            count = count + value + value * innerBagCount(key)
    return count

count = innerBagCount(search_key)
print("Total: " + str(count))
