#!/usr/bin/env python3
import re

with open('input_files/10.txt') as inputfile:
    instructions = inputfile.read().splitlines()

class Bot:
    def __init__(self, number, low_bot=None, high_bot=None):
        self.number = number
        self.low_bot = low_bot
        self.high_bot = high_bot
        self.values = []

def create_bots_with_rules(rules):
    rule_pattern = r'bot (\d+) gives low to bot (\d+) and ' \
                   r'high to bot (\d+)'
    rules = [r for r in rules if r.startswith('bot')]

    bots = {}
    for r in rules:
        m = re.match(rule_pattern, r)
        bots[m.group(1)] = Bot(m.group(1), m.group(2), m.group(3))

    return bots

print(create_bots_with_rules(instructions))
