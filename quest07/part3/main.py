file = open("input.txt", "r")

lines = file.readlines()
prefixes = lines[0].strip().split(",")

rules = {}
for line in lines[2:]:
    line = line.strip().split(" > ")
    rules[line[0]] = set(line[1].split(","))

total = 0
found = set()


def valid_names(prefix):
    if len(prefix) == 11:
        found.add(prefix)
        return

    if len(prefix) >= 7:
        found.add(prefix)

    for next in rules[prefix[-1]]:
        valid_names(prefix + next)


for prefix in prefixes:
    valid = True

    for letter in range(len(prefix) - 1):
        if prefix[letter] in rules:
            if prefix[letter + 1] not in rules[prefix[letter]]:
                valid = False
                break

    if valid:
        valid_names(prefix)

print(len(found))
print(total)
