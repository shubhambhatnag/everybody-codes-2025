file = open("input.txt", "r")
note = file.readlines()[0].strip() * 1000
n = len(note)
countA = countB = countC = 0

for i in range(1001):
    if note[i] == "A":
        countA += 1
    elif note[i] == "B":
        countB += 1
    elif note[i] == "C":
        countC += 1

total = 0
for soldier in range(n):
    if soldier > 0 and soldier + 1000 < n:
        if note[soldier + 1000] == "A":
            countA += 1
        elif note[soldier + 1000] == "B":
            countB += 1
        elif note[soldier + 1000] == "C":
            countC += 1

    if soldier - 1001 >= 0:
        if note[soldier - 1001] == "A":
            countA -= 1
        elif note[soldier - 1001] == "B":
            countB -= 1
        elif note[soldier - 1001] == "C":
            countC -= 1

    if note[soldier] == "a":
        total += countA
    elif note[soldier] == "b":
        total += countB
    elif note[soldier] == "c":
        total += countC

print(total)
