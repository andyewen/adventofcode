#!/usr/bin/env python3

with open('input.txt') as fp:
    print(sum(int(i) for i in fp.read().splitlines()))
