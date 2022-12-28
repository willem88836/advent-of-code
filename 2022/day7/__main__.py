
def build_entry(line):
    spl = line.split(" ")
    entry = {
        "is_command": spl[0] == "$",
    }
    if entry["is_command"]:
        entry["command"] = spl[1]
        if len(spl) == 3:
            entry["argument"] = spl[2]
    else:
        entry["is_dir"] = spl[0] == "dir"
        if entry["is_dir"]:
            entry["dir_name"] = spl[1]
        else:
            entry["file_name"] = spl[1]
            entry["file_size"] = int(spl[0])
    return entry


with open("./day7/input.txt", "r", encoding='utf-8') as input_file:
    data = [build_entry(line.strip()) for line in input_file.readlines()]


file_system = {}
current_directory = "/"


def add_directory(dir_name):
    file_system[dir_name] = 0


add_directory(current_directory)


def get_parent_dir(directory):
    if directory.endswith("/"):
        directory = directory[:-1]
    full_name = "/".join(directory.split("/")[:-1])
    full_name = f'{full_name}/'
    return full_name


def add_file(directory, file_size):
    file_system[directory] += file_size
    if directory != "/":
        parent_dir = get_parent_dir(directory[0:-1])
        add_file(parent_dir, file_size)


def handle_ls(start_index):
    dir_iterator = enumerate(data[start_index:], start=start_index)
    for next_index, dir_entry in dir_iterator:
        if dir_entry['is_command']:
            return next_index - 1
        elif dir_entry['is_dir']:
            dir_name = dir_entry['dir_name']
            new_dir = f'{current_directory}{dir_name}/'
            add_directory(new_dir)
        else:
            add_file(current_directory, dir_entry['file_size'])


iterator = enumerate(data)
for index, entry in iterator:
    if entry['command'] == 'ls':
        g = handle_ls(index + 1)
        # skips ls results
        for j, _ in iterator:
            if j == g:
                break
    if entry["command"] == "cd":
        match entry['argument']:
            case "/":
                current_directory = entry["argument"]
            case "..":
                current_directory = get_parent_dir(current_directory)
            case _:
                dir_name = entry['argument']
                current_directory = f'{current_directory}{dir_name}/'
                if not current_directory in file_system:
                    add_directory(current_directory)

total_size = 0
for dir_name, size in file_system.items():
    if size <= 100000:
        total_size += size
print(f'{total_size=}')


max_space = 70000000
needed_space = 30000000
available_space = max_space - file_system["/"]
cleared_space = needed_space - available_space
options = [size for size in file_system.values() if size >= cleared_space]
min_space = min(options)
print(f'{min_space=}')
