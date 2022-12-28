
def build_entry(line) -> dict:
    spl = line.strip().split(" ")
    return {
        "op": spl[0],
        "me": spl[1]
    }


with open("./day2/input.txt", "r", encoding="utf-8") as input_file:
    data = [build_entry(line) for line in input_file.readlines()]


scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

rps = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    }
}

guide = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y"
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z"
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X"
    }
}

TOTAL_SCORE = 0
REAL_TOTAL_SCORE = 0
for entry in data:
    ROUND_SCORE = 0
    my_act = entry["me"]
    op_act = entry["op"]
    TOTAL_SCORE += scores[my_act] + rps[op_act][my_act]
    gd_act = guide[op_act][my_act]
    REAL_TOTAL_SCORE += scores[gd_act] + rps[op_act][gd_act]

print(f'{TOTAL_SCORE=}')
print(f'{REAL_TOTAL_SCORE=}')
