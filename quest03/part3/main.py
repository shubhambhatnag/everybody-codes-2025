file = open("input.txt", "r")

boxes = sorted([int(i) for i in file.readlines()[0].strip().split(",")], reverse=True)

sets = 0
while boxes:
    sets += 1
    last = boxes[0]
    to_remove = [0]
    for box in range(1, len(boxes)):
        if boxes[box] < last:
            to_remove.append(box)
            last = boxes[box]

    for i in sorted(to_remove, reverse=True):
        del boxes[i]

print(sets)
