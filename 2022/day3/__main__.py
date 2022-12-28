
with open("./day3/input.txt", "r", encoding='utf-8') as input_data:
    data = [line.strip() for line in input_data.readlines()]

ITEM_TYPES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
item_priorities = {item_type: priority for priority,
                   item_type in enumerate(ITEM_TYPES, start=1)}

TOTAL_SCORE = 0
for entry in data:
    pivot = int(len(entry) / 2)
    left = set(entry[:pivot])
    right = set(entry[pivot:])
    intersect = list(left.intersection(right))[0]
    TOTAL_SCORE += item_priorities[intersect]

print(f'{TOTAL_SCORE=}')

TEAM_TOTAL_SCORE = 0
for index in range(0, len(data), 3):
    packs = [set(pack) for pack in data[index: index + 3]]
    intersect = list(packs[0].intersection(packs[1]).intersection(packs[2]))[0]
    TEAM_TOTAL_SCORE += item_priorities[intersect]

print(f'{TEAM_TOTAL_SCORE=}')
