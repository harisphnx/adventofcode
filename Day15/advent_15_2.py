with open("day_15_input.txt") as f:
    lines = f.readlines()

ingr, count, max_val = [[0 for i in range(5)] for i in range(4)], 0, -9999

for i in range(len(lines)):
    ingr[i][0]  = int(lines[i].rstrip().split(' ')[2][0:len(lines[i].rstrip().split(' ')[2])-1])
    ingr[i][1]  = int(lines[i].rstrip().split(' ')[4][0:len(lines[i].rstrip().split(' ')[4])-1])
    ingr[i][2]  = int(lines[i].rstrip().split(' ')[6][0:len(lines[i].rstrip().split(' ')[6])-1])
    ingr[i][3]  = int(lines[i].rstrip().split(' ')[8][0:len(lines[i].rstrip().split(' ')[8])-1])
    ingr[i][4]  = int(lines[i].rstrip().split(' ')[10][0:len(lines[i].rstrip().split(' ')[10])])

for i in range(100):
    for j in range(100):
        for k in range(100):
            l = 100 - (i + j + k)
            if(l >= 0):
                val = 1
                for x in range(4):
                    temp =  i*ingr[0][x] + j*ingr[1][x] + k*ingr[2][x] + l*ingr[3][x]
                    if(temp < 0):
                        temp = 0
                    val *= temp
                if(val > max_val and ( (i*ingr[0][4] + j*ingr[1][4] + k*ingr[2][4] + l*ingr[3][4]) == 500 ) ):
                    max_val = val
print max_val
