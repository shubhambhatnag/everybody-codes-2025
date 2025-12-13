file = open("input.txt", "r")

boxes = sorted([int(i) for i in file.readlines()[0].strip().split(",")])

total = set()

curr = 0
while len(total) != 20 and curr < len(boxes):
    total.add(boxes[curr])
    curr += 1
print(sum(total))
