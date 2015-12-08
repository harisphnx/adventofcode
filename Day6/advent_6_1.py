with open("day_6_input.txt") as f:
    commands = f.readlines()

arr = [[0 for i in range(1000)] for j in range(1000)]
comm_list = {"on": 1, "off": 0}

def helper(comm, x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] = comm_list[comm]

for x in commands:
    temp = x.rsplit()
    if( len(temp) == 4):
        for i in range(int(temp[1].split(",")[0]), int(temp[3].split(",")[0])+1):
            for j in range(int(temp[1].split(",")[1]), int(temp[3].split(",")[1])+1):
                arr[i][j] ^= 1
    else:
        helper(temp[1], int(temp[2].split(",")[0]), int(temp[2].split(",")[1]), int(temp[4].split(",")[0]), int(temp[4].split(",")[1]))

count = 0
for i in range(1000):
    for j in range(1000):
        if(arr[i][j] == 1):
             count += 1
print count
