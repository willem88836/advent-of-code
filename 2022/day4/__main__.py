

def build_entry(line: str):
    spl = line.split(",")
    elf_a = spl[0].split("-")
    elf_b = spl[1].split("-")
    return {
        "elf_a": {
            "start": int(elf_a[0]),
            "end": int(elf_a[1])
        },
        "elf_b": {
            "start": int(elf_b[0]),
            "end": int(elf_b[1])
        }
    }


with open("./day4/input.txt", 'r', encoding='utf-8') as input_file:
    data = [build_entry(line.strip()) for line in input_file.readlines()]

OVERLAP_COUNT = 0
PART_OVERLAP_COUNT = 0
for entry in data:
    if (entry['elf_a']['start'] >= entry['elf_b']['start'] and
        entry['elf_a']['end'] <= entry['elf_b']['end']) or \
        (entry['elf_b']['start'] >= entry['elf_a']['start'] and
         entry['elf_b']['end'] <= entry['elf_a']['end']):
        OVERLAP_COUNT += 1

    elf_a = set(range(entry['elf_a']['start'], entry['elf_a']['end'] + 1))
    elf_b = set(range(entry['elf_b']['start'], entry['elf_b']['end'] + 1))
    if len(elf_a.intersection(elf_b)):
        PART_OVERLAP_COUNT += 1

print(f'{OVERLAP_COUNT=}')
print(f'{PART_OVERLAP_COUNT=}')
