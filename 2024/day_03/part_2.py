import re

with open('input.txt') as in_file:
    content = in_file.read()

mul_re = re.compile(r'(do\(\))|(don\'t\(\))|(?:mul\((\d+),(\d+)\))')

results = mul_re.findall(content)
do = True 
result = 0
for do_match, dont_match, mul_a, mul_b in results:
    if do_match:
        do = True
    elif dont_match:
        do = False
    elif do:
        # Must be a mul match. Add the product of a and b if do is True.
        result += int(mul_a) * int(mul_b)

print(result)
