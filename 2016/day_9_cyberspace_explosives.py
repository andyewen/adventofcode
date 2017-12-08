#!/usr/bin/env python3
import re

marker_pattern = r'\((\d+)x(\d+)\)'

def decompress(s):
    m = re.search(marker_pattern, s)
    if m:
        num_chars = int(m.group(1))
        num_repeat = int(m.group(2))
        start = m.start()
        end = m.end()
        return (start + 
                decompress(s[end:end + num_chars] * num_repeat) +
                decompress(s[end + num_chars:]))
    else:
        return len(s)

def main():
    filename = 'input_files/9.txt'
    with open(filename) as inputfile:
        inputstring = inputfile.read()
        
    decompressed = decompress(re.sub(r'\s', '', inputstring))
    print(decompressed)
    
if __name__ == '__main__':
    main()


