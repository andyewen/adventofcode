# Written by Anna with help from Andrew

input_file = open('input.txt')
contents = input_file.read()

annalist = ['sammy', 'sandstorm', 'sooty', 'sweep', 'sox', 'soo']
n = 0
print(annalist[n])
s = '3'
s = int(s)
print(annalist[s])

leftlist = []
rightlist = []
for line in contents.splitlines():
    left = line[0:5]
    right = line[8:13]
    left = int(left)
    right = int(right)
    leftlist.append(left)
    rightlist.append(right)

total_value = 0
for left in leftlist:
    count = 0
    for right in rightlist:
        if right == left:
            count = count+1
    total_value = total_value + (left*count)
print(total_value)