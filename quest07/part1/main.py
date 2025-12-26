file = open("input.txt", "r")

lines = file.readlines()
names = lines[0].strip().split(",")

rules = {}
for line in lines[2:]:
    line = line.strip().split(" > ")
    rules[line[0]] = set(line[1].split(","))


for name in names:
    valid = True

    for letter in range(len(name) - 1):
        if name[letter] in rules:
            if name[letter + 1] not in rules[name[letter]]:
                valid = False
                break

    if valid:
        print(name)
        break
