
with open("./day6/input.txt", "r", encoding='utf-8') as input_file:
    data = input_file.read().strip()

def find_start_index(the_data, frame):
    for i in range(0, len(the_data) - frame):
        unique = set(iter(the_data[i: i + frame]))
        if len(unique) == frame:
            return i + frame

index = find_start_index(data, 4)
print(f'{index=}')
index2 = find_start_index(data,  14)
print(f'{index2=}')
