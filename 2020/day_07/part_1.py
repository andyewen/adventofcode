def bag_contains(rules, search_bag_type, current_bag_type):
    bag_contents = rules[current_bag_type]
    if not bag_contents:
        return False
    if search_bag_type in bag_contents:
        return True
    return any(
        bag_contains(rules, search_bag_type, bag_type)
        for bag_type in bag_contents
    )


with open('input.txt') as f:
    rules = {}
    for line in f:
        line = line.rstrip('.\n')
        bag, contains = line.split(' contain ')
        bag_type = ' '.join(bag.split()[0:2])
        bag_contents = []
        if contains != 'no other bags':
            for item in contains.split(', '):
                content_bag_type = ' '.join(item.split()[1:3])
                bag_contents.append(content_bag_type)
        rules[bag_type] = bag_contents


print(sum(bag_contains(rules, 'shiny gold', bag_type) for bag_type in rules.keys()))
