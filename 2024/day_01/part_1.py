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


leftlist.sort()
rightlist.sort()
total_value = 0
for n in range(0, len(leftlist)):
    left = leftlist[n]
    right = rightlist[n]
    
    difference = abs(left-right)
    total_value = total_value + difference

print(total_value)