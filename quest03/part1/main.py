file = open("input.txt", "r")

boxes = [int(i) for i in file.readlines()[0].strip().split(",")]

print(sum(set(boxes)))
