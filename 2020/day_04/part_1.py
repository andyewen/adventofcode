required_fields = {
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
}


def is_passport_valid(passport):
    # Passport finished.
    passport_fields = set(current_passport.keys())
    return passport_fields >= required_fields


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
