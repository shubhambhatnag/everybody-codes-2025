import math

file = open("input.txt", "r")


def ccw(a, b, c):
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])


def intersect_naive(a, b, c, d):
    # Proper intersection only (no touching endpoints)
    if a == c or a == d or b == c or b == d:
        return False

    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)


steps = [int(x) for x in file.readlines()[0].strip().split(",")]

n = 256
radius = 1.0

points = [
    (radius * math.cos(2 * math.pi * k / n), radius * math.sin(2 * math.pi * k / n))
    for k in range(n)
]

lines = []
knots = 0

for step in range(len(steps) - 1):
    total = 0
    for line in lines:
        a, b = line
        if len({a, b, points[steps[step] - 1], points[steps[step + 1] - 1]}) == 4:
            if intersect_naive(
                a, b, points[steps[step] - 1], points[steps[step + 1] - 1]
            ):
                total += 1

    knots += total

    lines.append((points[steps[step] - 1], points[steps[step + 1] - 1]))

print(knots)
