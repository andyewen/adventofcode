def add_pos(a, b):
    return (a[0] + b[0], a[1] + b[1])


def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def follow_wire(commands):
    visited = {}
    position = (0, 0)
    distance = 0
    for c in commands:
        direction = directions[c[0]]
        steps = int(c[1:])

        for _ in range(steps):
            distance += 1
            position = add_pos(position, direction)
            visited[position] = distance
    return visited


directions = {
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
    'U': (0, -1)
}

with open('input.txt') as f:
    file_contents = f.read()

wires = [line.split(',') for line in file_contents.splitlines()]
wire_1, wire_2, *_ = wires

wire_1_result = follow_wire(wire_1)
wire_2_result = follow_wire(wire_2)


# Get all the points that are in both wires.
intersections = (
    set(follow_wire(wire_1).keys()) &
    set(follow_wire(wire_2).keys())
)

# Find the minimum of the sum of both wire's distance at each intersection.
print(min(wire_1_result[i] + wire_2_result[i] for i in intersections))
