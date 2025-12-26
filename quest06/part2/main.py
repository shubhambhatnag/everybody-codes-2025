file = open("input.txt", "r")

note = file.readlines()[0].strip()

seen = [0, 0, 0]
total = 0
for soldier in note:
    if soldier == "A":
        seen[0] += 1
    if soldier == "B":
        seen[1] += 1
    if soldier == "C":
        seen[2] += 1

    elif soldier == "a":
        total += seen[0]
    elif soldier == "b":
        total += seen[1]
    elif soldier == "c":
        total += seen[2]
print(total)
