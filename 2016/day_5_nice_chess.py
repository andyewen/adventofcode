#!/usr/bin/env python3
from hashlib import md5

inputstring = 'ffykfhsq'

password = ['_'] * 8
index = 0

while not all(c != '_' for c in password):
    md5_hash = md5((inputstring + str(index)).encode()).hexdigest()
    if (md5_hash.startswith('00000') and md5_hash[5].isnumeric() and
            int(md5_hash[5]) < 8):
        position = int(md5_hash[5])
        if password[position] == '_':
            char = md5_hash[6]
            password[position] = char
            print(''.join(password))

    index += 1

print('Done!')

