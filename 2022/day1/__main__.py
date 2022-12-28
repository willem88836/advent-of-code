import numpy as np


with open("./day1/input.txt", 'r', encoding='utf-8') as input_data:
    data = [line.strip() for line in input_data.readlines()]

calories = []
cur_cals = 0
for entry in data:
    if len(entry) == 0:
        calories.append(cur_cals)
        cur_cals = 0
        continue
    cur_cals += int(entry)

mx = sorted(calories,reverse=True)[:3]
print(f'{mx=}')
sm = sum(mx)
print(f'{sm=}')
