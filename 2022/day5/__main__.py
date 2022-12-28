
def build_initial_stacks(initial_stack_lines):
    stride = 4
    line_length = len(initial_stack_lines[-1])
    initial_stacks = [[] for _ in range(int(line_length / stride))]
    for line in initial_stack_lines[::-1]:
        for i in range(1, line_length, stride):
            box = line[i]
            if box == ' ':
                continue
            idx = int(i / stride)
            initial_stacks[idx].append(box)
    return initial_stacks


def build_instructions(lines):
    instrs = []
    for line in lines:
        spl = line.strip().split(' ')
        instrs.append({
            'count': int(spl[1]),
            'from': int(spl[3]) - 1,
            'to': int(spl[5]) - 1
        })
    return instrs


with open("./day5/input.txt", "r", encoding='utf-8') as input_file:
    all_lines = input_file.readlines()
    stack_lines = all_lines[:8]
    stacks1 = build_initial_stacks(stack_lines)
    stacks2 = build_initial_stacks(stack_lines)
    instruction_lines = all_lines[10:]
    instructions = build_instructions(instruction_lines)

for move in instructions:
    for _ in range(move['count']):
        box = stacks1[move['from']].pop()
        stacks1[move['to']].append(box)


def get_output(stacks):
    output = ""
    for stack in stacks:
        output = f'{output}{stack[-1]}'
    return output


output1 = get_output(stacks1)
print(f'{output1=}')

for move in instructions:
    end = len(stacks2[move['from']]) - move['count']
    boxes = stacks2[move['from']][end:]
    stacks2[move['to']].extend(boxes)
    stacks2[move['from']] = stacks2[move['from']][:end]


output2 = get_output(stacks2)
print(f'{output2=}')
