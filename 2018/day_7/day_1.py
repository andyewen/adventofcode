#!/usr/bin/env python3
import fileinput
import bisect


def get_all_nodes(verts):
    # Get a set of all the node letters.
    return set(node for vert in verts for node in vert)


def find_roots(verts):
    # Get a set of all the nodes that don't depend on anything.
    seen_children = set(child for child, *_ in verts)
    return get_all_nodes(verts) - seen_children


def get_parents(child_node, verts):
    return set(parent for child, parent in verts if child == child_node)


def get_children(parent_node, verts):
    return set(child for child, parent in verts if parent == parent_node)


verts = []
for line in fileinput.input():
    words = line.split()
    verts.append((words[7], words[1]))

# Initialise sorted working list.
output_str = ''
working_list = sorted(find_roots(verts))

while len(working_list):
    remove_index = None
    for i, node in enumerate(working_list):
        parents = get_parents(node, verts)
        if not parents or all(p in output_str for p in parents):
            remove_index = i
            break
    node = working_list.pop(remove_index)
    output_str += node
    for child in get_children(node, verts):
        # Insert child into working list while maintaining order.
        if child not in working_list:
            bisect.insort_left(working_list, child)

print('The answer is:')
print(output_str)
