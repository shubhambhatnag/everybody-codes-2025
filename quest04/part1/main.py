file = open("input.txt", "r")

gears = [int(line.strip()) for line in file.readlines()]

rotations = 2025
for i in range(1, len(gears)):
    rotations *= gears[i - 1] / gears[i]

print(int(rotations))
