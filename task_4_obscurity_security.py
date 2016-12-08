#!/usr/bin/env python3

import re
from collections import defaultdict
from operator import itemgetter

def validate_code(name, checksum):
    letter_count = defaultdict(int)
    name = name.replace('-', '')
    for letter in name:
        letter_count[letter] += 1
        
    letter_count = list(letter_count.items())
    
    # Sort alphabetically first then by count.
    letter_count.sort(key=itemgetter(0))
    letter_count.sort(key=itemgetter(1), reverse=True)
    
    top_five_letters = [i[0] for i in letter_count][:5]
    return ''.join(top_five_letters) == checksum

def main():
    with open('input_files/4.txt') as inputfile:
        codes = inputfile.readlines()
    
    pattern = '(?P<name>[a-z\-]+)(?P<sector_id>\d+)\[(?P<checksum>[a-z]+)\]'

    sum = 0
    for code in codes:
        m = re.match(pattern, code)
        if m:
            g = m.groupdict()
            name, sector_id, checksum = g['name'], g['sector_id'], g['checksum']
            if validate_code(name, checksum):
                sum += int(sector_id)
    
    print(sum)

if __name__ == '__main__':
    main()
