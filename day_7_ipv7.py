#!/usr/bin/env python3
import re

filename = 'input_files/7.txt'
with open(filename) as inputfile:
    addresses = inputfile.read().splitlines()

abba_length = 4

def is_abba(sequence):
    for i in range(len(sequence) - (abba_length - 1)):
        potential_abba = sequence[i:i+abba_length]
        if (potential_abba[0] != potential_abba[1] and
                potential_abba == potential_abba[::-1]):
            return True

    return False

def address_supports_tls(address):
    hypernet_seqs = re.findall(r'\[(\w+)\]', address)
    non_hypernet_seqs = re.split(r'\[\w+\]', address)
    return (any(is_abba(seq) for seq in non_hypernet_seqs) and
        not any(is_abba(seq) for seq in hypernet_seqs))

print(sum(address_supports_tls(address) for address in addresses))
