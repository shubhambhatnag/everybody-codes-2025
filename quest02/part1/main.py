file = open("input.txt", "r")

A = tuple([int(i) for i in file.readlines()[0].strip().split("=")[1][1:-1].split(",")])


def multiply(p1, p2):
    X1, Y1 = p1
    X2, Y2 = p2

    return (X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2)


def divide(p1, p2):
    X1, Y1 = p1
    X2, Y2 = p2

    return (X1 // X2, Y1 // Y2)


def add(p1, p2):
    X1, Y1 = p1
    X2, Y2 = p2

    return (X1 + X2, Y1 + Y2)


curr = (0, 0)

for i in range(3):
    curr = multiply(curr, curr)
    curr = divide(curr, (10, 10))
    curr = add(curr, A)

print(list(curr))
