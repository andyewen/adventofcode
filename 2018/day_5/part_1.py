#!/usr/bin/env python3


def process_step(s):
    new_string = ''
    i = 0
    while i < (len(s) - 1):
        char_1 = s[i]
        char_2 = s[i + 1]
        if char_1.lower() == char_2.lower() and char_1 != char_2:
            i += 2
        else:
            new_string += char_1
            i += 1
    new_string += s[-1]
    return new_string


def process_polymer(input_string):
    old_string = input_string
    while 1:
        new_string = process_step(old_string)
        if len(new_string) == len(old_string):
            break
        old_string = new_string

    return new_string


with open('input.txt') as fp:
    input_string = fp.read().rstrip()

result = process_polymer(input_string)
print(f'There are {len(result)} units in the final string.')
