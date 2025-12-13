file = open("input.txt", "r")

A = tuple([int(i) for i in file.readlines()[0].strip().split("=")[1][1:-1].split(",")])


def multiply(p1, p2):
    X1, Y1 = p1
    X2, Y2 = p2

    return (X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2)


def divide(p1, p2):
    X1, Y1 = p1
    X2, Y2 = p2

    return (int(X1 / X2), int(Y1 / Y2))


def add(p1, p2):
    X1, Y1 = p1
    X2, Y2 = p2

    return (X1 + X2, Y1 + Y2)


B = add(A, (1000, 1000))

cnt = 0
engraved = set()
for X in range(A[0], B[0] + 1):
    for Y in range(A[1], B[1] + 1):
        exceeded = False
        if (Y, X) in engraved:
            cnt += 1
            continue
        curr = (0, 0)
        for i in range(100):
            curr = multiply(curr, curr)
            curr = divide(curr, (100000, 100000))
            curr = add(curr, (X, Y))

            if not (-1000000 <= curr[0] <= 1000000 and -1000000 <= curr[1] <= 1000000):
                exceeded = True
                break

        if not exceeded:
            engraved.add((X, Y))
            cnt += 1


print(cnt)
