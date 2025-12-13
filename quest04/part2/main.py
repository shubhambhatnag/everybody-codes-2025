file = open("input.txt", "r")

gears = [int(line.strip()) for line in file.readlines()]

ratio = 1
for i in range(1, len(gears)):
    ratio *= gears[i - 1] / gears[i]

print(round(10000000000000 / ratio))
