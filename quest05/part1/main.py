file = open("input.txt", "r")

nums = [int(i) for i in file.readlines()[0].strip().split(":")[1].split(",")]

fishbone = []

for num in nums:
    placed = False
    for i in range(len(fishbone)):
        left, spine, right = fishbone[i]

        if num < spine and left is None:
            fishbone[i][0] = num
            placed = True
            break
        elif num > spine and right is None:
            fishbone[i][2] = num
            placed = True
            break
    if not placed:
        fishbone.append([None, num, None])

num = ""
for line in fishbone:
    num += str(line[1])

print(num)
