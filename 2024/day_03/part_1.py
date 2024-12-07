import re

with open('input.txt') as in_file:
    content = in_file.read()

mul_re = re.compile(r'mul\((\d+),(\d+)\)')

results = mul_re.findall(content)
print(sum(int(a) * int(b) for a, b in results))
