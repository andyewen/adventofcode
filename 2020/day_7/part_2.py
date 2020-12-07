def count_bag(rules, current_bag_type):
    bag_contents = rules[current_bag_type]
    if not bag_contents:
        return 1
    return 1 + sum(
        n * count_bag(rules, bag_type) for bag_type, n in bag_contents.items()
    )


with open('input.txt') as f:
    rules = {}
    for line in f:
        line = line.rstrip('.\n')
        bag, contains = line.split(' contain ')
        bag_type = ' '.join(bag.split()[0:2])
        bag_contents = {}
        if contains != 'no other bags':
            for item in contains.split(', '):
                split_item = item.split()
                number = int(split_item[0])
                content_bag_type = ' '.join(split_item[1:3])
                bag_contents[content_bag_type] = number
        rules[bag_type] = bag_contents


print(count_bag(rules, 'shiny gold') - 1)
