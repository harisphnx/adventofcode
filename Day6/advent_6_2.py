with open("day_6_input.txt") as f:
    commands = f.readlines()

arr = [[0 for i in range(1000)] for j in range(1000)]

def helper(comm, x1, y1, x2, y2):
    if(comm == "on"):
        change = 1
    elif(comm == "off"):
        change = -1
    else:
        change = 2
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] += change
            if(arr[i][j] < 0):
                arr[i][j] = 0

for x in commands:
    temp = x.rsplit()
    if( len(temp) == 4):
        helper(temp[0], int(temp[1].split(",")[0]), int(temp[1].split(",")[1]), int(temp[3].split(",")[0]), int(temp[3].split(",")[1]))
    else:
        helper(temp[1], int(temp[2].split(",")[0]), int(temp[2].split(",")[1]), int(temp[4].split(",")[0]), int(temp[4].split(",")[1]))

count = 0
for i in range(1000):
    for j in range(1000):
        count += arr[i][j]
print count
