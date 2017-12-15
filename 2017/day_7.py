#!/usr/bin/env python3

import re
from pprint import pprint

node_pattern = re.compile(r'^(?P<name>\w+)\s\((?P<weight>\d+)\)(?:\s->\s(?P<children>[\w,\s]+))?$')

def parse_line(line):
    match_dict = node_pattern.match(line).groupdict()

    children = match_dict['children']
    if children is not None:
        children = children.split(', ')
    else:
        children = []

    return {
        'name': match_dict['name'],
        'weight': int(match_dict['weight']),
        'children':  children
    }

with open('input_files/7.txt') as f:
    nodes = [parse_line(line.strip()) for line in f.readlines()]

for n in nodes:
    found = False
    for o in nodes:
        if n['name'] in o['children']:
            found = True
            break

    if not found:
        break

print(n)
