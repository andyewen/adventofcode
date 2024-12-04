left_list = []
right_list = []

with open('input.txt') as input_file:
    for line in input_file:
        # Remove leading and trailing whitespace including newline character at end of line.
        line = line.strip()

        # Split the line into separate strings using any whitespace as a deliminator and convert
        # each string into an integer.
        numbers = (int(n) for n in line.split())

        # Unpack the 2 expected numbers from the structure into 2 variables and append them to respective lists.
        left, right = numbers
        left_list.append(left)
        right_list.append(right)

# Sort the two lists.
left_list.sort()
right_list.sort()

# Calculate the sum of the differences between the paired up items in the sorted lists.
total_difference = sum(
    abs(l - r)
    for l, r in zip(left_list, right_list)
)
print(f'{total_difference=}')
