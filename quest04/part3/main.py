file = open("input.txt", "r")

gears = [line.strip() for line in file.readlines()]

ratio = 1
for i in range(1, len(gears)):
    if i - 1 == 0:
        prev = int(gears[i - 1])
    else:
        prev = int(gears[i - 1].split("|")[1])

    if i == len(gears) - 1:
        curr = int(gears[i])
    else:
        curr = int(gears[i].split("|")[0])

    ratio *= prev / curr

print(100 * ratio)
