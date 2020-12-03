
# Advent of Code day 3

entry_file = open("./data/day-3.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)
forest_width = len(entries[0]) - 1

# Part 1

tree_count = 0
x_coord = 0 
y_coord = 0

x_jump = 3
y_jump = 1

while y_coord < entry_count: 
    row = entries[y_coord]
    position = row[x_coord]

    if (position == '#'): 
        tree_count += 1

    y_coord += y_jump
    x_coord = (x_coord + x_jump) % forest_width

print("Number of trees: " + str(tree_count))


# Part 2

x_jumps = [1, 3, 5, 7, 1]
y_jumps = [1, 1, 1, 1, 2]
trees = [0, 0, 0, 0, 0]

for i in range(0, len(x_jumps)):
    x_jump = x_jumps[i]
    y_jump = y_jumps[i]
    tree_count = 0
    x_coord = 0 
    y_coord = 0

    while y_coord < entry_count: 
        row = entries[y_coord]
        position = row[x_coord]

        if (position == '#'): 
            tree_count += 1

        y_coord += y_jump
        x_coord = (x_coord + x_jump) % forest_width

    print("Number of trees: " + str(tree_count))
    trees[i] = tree_count

product = 1
for i in trees:
    product *= i

print("Tree product: " + str(product))

