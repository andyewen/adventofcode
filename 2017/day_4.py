#!/usr/bin/env python3

with open('input_files/4.txt') as f:
    passphrases = list(f)


def passphrase_is_valid(p):
    seen = set()
    for word in p.split():
        sorted_word = ''.join(sorted(word))
        if sorted_word in seen:
            return False
        seen.add(sorted_word)
    return True


print(sum(passphrase_is_valid(p) for p in passphrases))
