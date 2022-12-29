
with open("./day8/input.txt", "r", encoding="utf-8") as input_file:
    data = [[int(tree) for tree in row.strip()]
            for row in input_file.readlines()]

size = len(data)
visible_trees = 0
for row in range(size):
    for col in range(size):
        directions = [
            data[row][:col],
            data[row][col + 1:],
            [r[col] for r in data[:row]],
            [r[col] for r in data[row + 1:]]
        ]
        tree_height = data[row][col]
        for direction in directions:
            tree_is_visible = True
            for tree in direction:
                if tree_height <= tree:
                    tree_is_visible = False
                    break
            if tree_is_visible:
                visible_trees += 1
                break

print(f'{visible_trees=}')

max_scenic_score = 0
for row in range(1, size - 1):
    for col in range(1, size - 1):
        directions = [
            data[row][:col][::-1],  # rhs
            data[row][col + 1:],  # lhs
            [r[col] for r in data[:row]][::-1],  # uhs
            [r[col] for r in data[row + 1:]]  # bhs
        ]
        tree_height = data[row][col]
        total_scenic_score = 1
        for direction in directions:
            scenic_score = 0
            for tree in direction:
                scenic_score += 1
                if tree >= tree_height:
                    break
            total_scenic_score *= scenic_score
        max_scenic_score = max(max_scenic_score, total_scenic_score)

print(f'{max_scenic_score=}')
