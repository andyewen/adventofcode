#!/usr/bin/env python3

import re
from collections import defaultdict
from operator import itemgetter
from pprint import pprint

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

def shift_cipher_name(name, shift_amount):
    name = name.replace('-', ' ')
    shifted_name = ''
    for c in name:
        if c.isalpha():
            c = c.lower()
            num = ord(c) - 97
            num = (num + shift_amount) % 26
            shifted_name += chr(num + 97)
        else:
            shifted_name += c
            
    return shifted_name

def main():
    with open('input_files/4.txt') as inputfile:
        codes = inputfile.readlines()
    
    pattern = '(?P<name>[a-z\-]+)\-(?P<sector_id>\d+)\[(?P<checksum>[a-z]+)\]'

    sum = 0
    valid_code_names = {}
    for code in codes:
        m = re.match(pattern, code)
        if m:
            g = m.groupdict()
            name, sector_id, checksum = g['name'], g['sector_id'], g['checksum']
            if validate_code(name, checksum):
                sum += int(sector_id)
                valid_code_names[shift_cipher_name(name, int(sector_id))] = sector_id
    
    pprint(valid_code_names)
    

if __name__ == '__main__':
    main()
