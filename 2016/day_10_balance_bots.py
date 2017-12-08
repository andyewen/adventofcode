#!/usr/bin/env python3
import re


class Bucket:
    def __init__(self, identifier, low_bucket=None, high_bucket=None):
        self.identifier = identifier
        self.low_bucket = low_bucket
        self.high_bucket = high_bucket
        self.values = []

    def give(self, value, buckets):
        self.values.append(value)
        if len(self.values) >= 2 and self.identifier.startswith('bot'):
            low_bucket = buckets.get(self.low_bucket)
            high_bucket = buckets.get(self.high_bucket)
            if low_bucket:
                low_bucket.give(min(self.values), buckets)
            if high_bucket:
                high_bucket.give(max(self.values), buckets)
            self.values = []

    def __str__(self):
        return "{}: {}".format(self.identifier, self.values)


def create_buckets_with_rules(instructions):
    rules = [i for i in instructions if i.startswith('bot')]
    rule_pattern = r'(\w+ \d+) gives low to (\w+ \d+) and ' \
                   r'high to (\w+ \d+)'

    buckets = {}
    for r in rules:
        m = re.match(rule_pattern, r)
        low_bucket, high_bucket = m.group(2), m.group(3)
        buckets[m.group(1)] = Bucket(m.group(1), low_bucket, high_bucket)
        if not low_bucket in buckets:
            buckets[low_bucket] = Bucket(low_bucket)
        if not high_bucket in buckets:
            buckets[high_bucket] = Bucket(high_bucket)

    return buckets


def give_buckets_values(buckets, instructions):
    initials = [i for i in instructions if i.startswith('value')]
    initial_pattern = r'value (\d+) goes to (\w+ \d+)'

    for i in initials:
        m = re.match(initial_pattern, i)
        buckets[m.group(2)].give(int(m.group(1)), buckets)


def main():
    with open('input_files/10.txt') as inputfile:
        instructions = inputfile.read().splitlines()

    buckets = create_buckets_with_rules(instructions)
    give_buckets_values(buckets, instructions)

    print(sorted([str(bucket) for bucket in buckets.values()
                  if bucket.identifier.startswith('output')]))


if __name__ == '__main__':
    main()
