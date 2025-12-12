file = open("input.txt", "r")

lines = file.readlines()

names = lines[0].strip().split(",")
steps = lines[2].strip().split(",")

curr = 0

for step in steps:
    if step[0] == "L":
        curr -= int(step[1:])
    else:
        curr += int(step[1:])

    curr %= len(names)

print(names[curr])
