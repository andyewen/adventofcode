#!/usr/bin/env python3
import re

filename = 'input_files/7.txt'
with open(filename) as inputfile:
    addresses = inputfile.read().splitlines()

def n_length_substrings(s, n):
    for i in range(len(s) - (n - 1)):
        yield s[i:i+n]

def abas_and_babs(s):
    for substr in n_length_substrings(s, 3):
        if substr[0] == substr[-1] and substr[0] != substr[1]:
            yield substr

def invert(s):
    return ''.join([s[1], s[0], s[1]])

def address_supports_ssl(address):
    supernet_seqs = re.split(r'\[\w+\]', address)
    hypernet_seqs = re.findall(r'\[(\w+)\]', address)

    abas = set(aba for s in supernet_seqs for aba in abas_and_babs(s))
    babs = set(aba for s in hypernet_seqs for aba in abas_and_babs(s))

    return any((invert(bab) in abas) for bab in babs)

print(len(addresses))
print(sum(address_supports_ssl(address) for address in addresses))

