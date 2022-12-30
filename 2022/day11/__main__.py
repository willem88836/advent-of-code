import math
import copy


def add(x, y):
    if y == None:
        y = x
    return x + y


def mul(x, y):
    if y == None:
        y = x
    return x * y


def build_entry(lines: 'list[str]'):
    lines = [line.strip() for line in lines]
    monkey = lines[0][:-1]
    starting_items = [int(worry.strip(","))
                      for worry in lines[1].split(" ")[2:]]
    operation = add if lines[2][21] == "+" else mul
    operation_arg = lines[2].split(" ")[-1]
    operation_arg = None if operation_arg == "old" else int(operation_arg)
    test = int(lines[3].split(" ")[-1])
    target_true = int(lines[4].split(" ")[-1])
    target_false = int(lines[5].split(" ")[-1])

    return {
        "name": monkey,
        "items": starting_items,
        "operation": operation,
        "operation_arg": operation_arg,
        "test": test,
        "target_true": target_true,
        "target_false": target_false
    }


with open("day11/input.txt", "r", encoding='utf-8') as input_file:
    lines = input_file.readlines()
    stride = 7
    data = [build_entry(lines[index * stride: (index + 1) * stride - 1])
            for index, _ in enumerate(lines[::stride])]
    data_copy = copy.deepcopy(data)


def solution(is_part_2):
    monkey_inspects = {monkey['name']: 0 for monkey in data}
    rounds = 10000 if is_part_2 else 20

    lcm = math.lcm(*list([monkey['test'] for monkey in data]))

    for _ in range(rounds):
        for monkey in data:
            for item in monkey['items']:
                new_item = monkey["operation"](item, monkey['operation_arg'])
                if is_part_2:
                    new_item = new_item % lcm
                else:
                    new_item = int(new_item / 3)
                if new_item % monkey['test'] == 0:
                    data[monkey['target_true']]["items"].append(new_item)
                else:
                    data[monkey['target_false']]["items"].append(new_item)
                monkey['items'] = []
                monkey_inspects[monkey['name']] += 1

    highest = sorted(list(monkey_inspects.values()), key=lambda x: -x)
    monkey_business = highest[0] * highest[1]
    print(f'{monkey_business=}')


solution(False)
data = data_copy
solution(True)
