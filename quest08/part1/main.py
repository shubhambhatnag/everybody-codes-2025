file = open("input.txt", "r")

steps = [int(x) for x in file.readlines()[0].strip().split(",")]

center = 0
for step in range(len(steps) - 1):
    if abs(steps[step + 1] - steps[step]) == 16:
        center += 1

print(center)
