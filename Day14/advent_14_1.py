with open("day_14_input.txt") as f:
    lines = f.readlines()

deer_info, count, sec, max_dist = [[0 for i in range(5)] for i in range(9)], 0, 0, -9999

for line in lines:
    deer_info[count][0] = int(line.rstrip().split(' ')[3])
    deer_info[count][1] = int(line.rstrip().split(' ')[6])
    deer_info[count][2] = int(line.rstrip().split(' ')[13])
    count += 1

while(sec != 2503):
    for deer in deer_info:
        if(deer[3] == deer[1]):
            deer[3] = -deer[2]
        if(deer[3] >= 0):
            deer[4] += deer[0]
            if(deer[4] > max_dist):
                max_dist = deer[4]
        deer[3] += 1
    sec += 1
print max_dist
