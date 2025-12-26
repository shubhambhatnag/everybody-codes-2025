file = open("input.txt", "r")

note = file.readlines()[0].strip()

knights_seen = 0

total = 0
for soldier in note:
    if soldier == "A":
        knights_seen += 1
    elif soldier == "a":
        total += knights_seen

print(total)
