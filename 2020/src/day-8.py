
# Advent of Code day 8

entry_file = open("./data/day-8.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)


# Part 1

pointer = 0
counter = 0

def jmp(pointer, counter, args):
    return pointer + args, counter
def acc(pointer, counter, args): 
    return pointer + 1, counter + args
def nop(pointer, counter, args): 
    return pointer + 1, counter

passed_instructions = [0] * entry_count

while pointer != -1: 
    if passed_instructions[pointer] > 0: 
        break

    passed_instructions[pointer] += 1
    instruction = entries[pointer].strip().split(" ")
    operator = instruction[0]
    operand = int(instruction[1])

    method = globals()[operator]
    pointer, counter = method(pointer, counter, operand)

print("Counter: " + str(counter))


# Part 2

for corruption_pointer in range(0, entry_count):
    pointer = 0
    counter = 0
    corruption_count = 0
    passed_instructions = [0] * entry_count
    
    while pointer != -1: 
        if pointer < 0 or pointer >= entry_count or passed_instructions[pointer] > 0: 
            break

        passed_instructions[pointer] += 1
        instruction = entries[pointer].strip().split(" ")
        operator = instruction[0]
        operand = int(instruction[1])

        if operator == 'jmp' or operator == 'nop': 
            if corruption_count == corruption_pointer: 
                if operator == 'jmp': 
                    operator = 'nop'
                else: 
                    operator = 'jmp'
            corruption_count += 1

        method = globals()[operator]    
        pointer, counter = method(pointer, counter, operand)

    
    if pointer >= entry_count: 
        print("Corrupted Instruction: " + str(corruption_pointer))
        print("Counter: " + str(counter))
        break
