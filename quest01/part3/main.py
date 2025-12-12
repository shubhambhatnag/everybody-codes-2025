file = open("input.txt", "r")

lines = file.readlines()

names = lines[0].strip().split(",")
steps = lines[2].strip().split(",")


for step in steps:
    if step[0] == "L":
        swap = -1 * int(step[1:])
    else:
        swap = int(step[1:])

    swap %= len(names)
    names[0], names[swap] = names[swap], names[0]

print(names[0])
