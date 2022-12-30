
cycles = {
    "noop": 1,
    "addx": 2
}


def build_entry(line):
    spl = line.split(" ")
    entry = {
        "command": spl[0]
    }
    if len(spl) > 1:
        entry["arg"] = int(spl[1])
    return entry


with open("./day10/input.txt", "r", encoding='utf-8') as input_file:
    data = [build_entry(line.strip()) for line in input_file.readlines()]

cycle_start_offset = 20
cycle_track_interval = 40
tracked_cycles = []
x_register = 1
total_cycles = 1

screen_width = 40
screen_pointer = 1
screen_output = ""


def cycle_is_tracked():
    return (total_cycles - cycle_start_offset) % cycle_track_interval == 0


def add_tracked_cycle():
    result = x_register * total_cycles
    tracked_cycles.append(result)

def draw_cycle():
    global screen_pointer, screen_output
    if lies_between(screen_pointer + 1, x_register, x_register + 2):
        screen_output = f'{screen_output}#'
    else:
        screen_output = f'{screen_output}.'
    screen_pointer += 1
    if (total_cycles - 1) % screen_width == 0:
        screen_output = f'{screen_output}\n'
        screen_pointer = 1


def lies_between(x, a, b):
    return x >= a and x <= b

def handle_new_cycle():
    global total_cycles
    total_cycles += 1
    # update during idle cycles.
    if cycle_is_tracked():
        add_tracked_cycle()
    draw_cycle()


for entry in data:
    command = entry['command']
    used_cycles = cycles[command]

    for _ in range(used_cycles - 1):
        handle_new_cycle()

    # Apply action
    match command:
        case "noop":
            pass
        case "addx":
            # print(entry['arg'])
            x_register += entry['arg']

    # update after cycle completion
    handle_new_cycle()

total_tracked = sum(tracked_cycles)
print(f'{total_tracked=}')
print(screen_output)