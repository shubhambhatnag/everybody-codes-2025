file = open("input.txt", "r")

swords = []
for line in file.readlines():
    nums = [int(i) for i in line.strip().split(":")[1].split(",")]
    id = int(line.strip().split(":")[0])
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
    rows = []
    for spine in fishbone:
        row = ""
        if spine[0]:
            row += str(spine[0])
        if spine[1]:
            row += str(spine[1])
        if spine[2]:
            row += str(spine[2])
        rows.append(int(row))
        num += str(spine[1])

    num = int(num)

    swords.append((num, rows, id))

swords.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

checksum = 0
for i in range(len(swords)):
    checksum += swords[i][2] * (i + 1)

print(checksum)
