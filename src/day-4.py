
# Advent of Code day 4

entry_file = open("./data/day-4.dat","r")
entries = entry_file.readlines()
entry_count = len(entries)


# Part 1

valid_passports = 0
current_passport = 1

keys = dict({"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": False})
valid_fields = 0

for i in range(0, entry_count): 
    entry = entries[i]
    if len(entry) < 4:
        valid = valid_fields == 8 or (valid_fields == 7 and not keys["cid"])
        if valid: 
            valid_passports += 1
        
        keys = dict({"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": False})
        valid_fields = 0
        current_passport += 1
        continue

    split = entry.split(' ')
    
    for j in range(0, len(split)): 
        pair = split[j].split(':')
        key = pair[0]

        valid_fields += 1
        keys[key] = True

print("Valid Passports: " + str(valid_passports))


# Part 2  

def byr(args):
    year = int(args)
    return (year >= 1920 and year <= 2002)
def iyr(args):
    year = int(args)
    return (year >= 2010 and year <= 2020)
def eyr(args):
    year = int(args)
    return (year >= 2020 and year <= 2030)
def hgt(args):
    try: 
        symbol_count = len(args)
        hgt = int(args[0:symbol_count-2])
        if args[symbol_count - 1] == 'n': 
            return (hgt >= 59 and hgt <= 76)
        else:
            return (hgt >= 150 and hgt <= 193)
    except:
        return False
def hcl(args):
    if args[0] == '#' and len(args) == 7: 
        valid_symbols = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f', '\n']
        for i in range(1, len(args)): 
            symbol = args[i]
            isValid = False
            for j in range(0, len(valid_symbols)):
                if symbol == valid_symbols[j]: 
                    isValid = True
            if not isValid: 
                print(args)
                return False
        return True
    return False
def ecl(args):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for i in range(0, len(valid_colors)): 
        if args == valid_colors[i]: 
            return True
    return False
def pid(args):
    try: 
        int(args)
        return len(args) == 9
    except:
        return False
def cid(args):
    return True

valid_passports = 0
current_passport = 1

keys = dict({"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": False})
test = dict({"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid, "cid": cid})
valid_fields = 0

for i in range(0, entry_count): 
    entry = entries[i]
    if len(entry) < 4:
        valid = valid_fields == 8 or (valid_fields == 7 and not keys["cid"])
        if valid: 
            valid_passports += 1
        
        keys = dict({"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": False})
        valid_fields = 0
        current_passport += 1
        continue

    split = entry.split(' ')
    
    for j in range(0, len(split)): 
        pair = split[j].split(':')
        key = pair[0]
        value = pair[1]
        if value[len(value) - 1] == '\n': 
            value = value[0:len(value) - 1]

        method = test[key]
        valid = method(value)

        if valid: 
            valid_fields += 1
            keys[key] = True

print("Valid Passports: " + str(valid_passports))
