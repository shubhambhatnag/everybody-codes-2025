file = open("input.txt", "r")

lines = file.readlines()
names = lines[0].strip().split(",")

rules = {}
for line in lines[2:]:
    line = line.strip().split(" > ")
    rules[line[0]] = set(line[1].split(","))

total = 0
cnt = 0
for name in names:
    cnt += 1
    valid = True

    for letter in range(len(name) - 1):
        if name[letter] in rules:
            if name[letter + 1] not in rules[name[letter]]:
                valid = False
                break

    if valid:
        total += cnt

print(total)
