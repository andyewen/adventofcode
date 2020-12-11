import re

hgt_regex = re.compile(r'^(\d+)(cm|in)$')
hcl_regex = re.compile(r'^#[0-9a-f]{6,6}$')
valid_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
pid_regex = re.compile(r'^\d{9,9}$')

required_fields = {
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
}


def is_field_valid(field, value):
    if field == 'byr':
        return 1920 <= int(value) <= 2002
    elif field == 'iyr':
        return 2010 <= int(value) <= 2020
    elif field == 'eyr':
        return 2020 <= int(value) <= 2030
    elif field == 'hgt':
        match = hgt_regex.match(value)
        if not match:
            return False
        number, unit = match.group(1, 2)
        number = int(number)
        if unit == 'cm':
            return 150 <= number <= 193
        elif unit == 'in':
            return 59 <= number <= 76
        return False
    elif field == 'hcl':
        return bool(hcl_regex.match(value))
    elif field == 'ecl':
        return value in valid_ecl
    elif field == 'pid':
        return bool(pid_regex.match(value))
    return True


def is_passport_valid(passport):
    passport_fields = set(passport.keys())
    if not passport_fields >= required_fields:
        return False
    for key, value in passport.items():
        if not is_field_valid(key, value):
            return False
    return True


valid_count = 0

with open('input.txt') as f:
    current_passport = {}
    for line in f:
        line = line.rstrip('\n')
        if line:
            pairs = line.split()
            for pair in pairs:
                key, value = pair.split(':', maxsplit=1)
                current_passport[key] = value
        else:
            if is_passport_valid(current_passport):
                valid_count += 1
            current_passport = {}
    if is_passport_valid(current_passport):
        valid_count += 1

print(valid_count)
