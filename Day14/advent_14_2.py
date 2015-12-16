with open("day_14_input.txt") as f:
    lines = f.readlines()

deer_info, count, sec, max_dist, max_point = [[0 for i in range(6)] for i in range(9)], 0, 0, -9999, -9999

for line in lines:
    deer_info[count][0] = int(line.rstrip().split(' ')[3])
    deer_info[count][1] = int(line.rstrip().split(' ')[6])
    deer_info[count][2] = int(line.rstrip().split(' ')[13])
    count += 1

while(sec != 2503):
    for i in range(len(deer_info)):
        if(deer_info[i][3] == deer_info[i][1]):
            deer_info[i][3] = -deer_info[i][2]
        if(deer_info[i][3] >= 0):
            deer_info[i][4] += deer_info[i][0]
            if(deer_info[i][4] >= max_dist):
                max_dist = deer_info[i][4]
        deer_info[i][3] += 1
    for deer in deer_info:
        if(deer[4] == max_dist):
            deer[5] += 1
            if(deer[5] > max_point):
                max_point = deer[5]
    sec += 1
print max_point
