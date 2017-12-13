#!/usr/bin/env python3

with open('input_files/4.txt') as f:
    passphrases = list(f)


def passphrase_is_valid(p):
    seen = set()
    for word in p.split():
        if word in seen:
            return False
        seen.add(word)
    return True


print(sum(passphrase_is_valid(p) for p in passphrases))
