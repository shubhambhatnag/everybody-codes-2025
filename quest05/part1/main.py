file = open("input.txt", "r")

smallest = None
largest = None
for line in file.readlines():
    nums = [int(i) for i in line.strip().split(":")[1].split(",")]

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
    for spine in fishbone:
        num += str(spine[1])

    num = int(num)

    if largest is None:
        largest = num
    else:
        largest = max(largest, num)

    if smallest is None:
        smallest = num
    else:
        smallest = min(smallest, num)
print(largest - smallest)
