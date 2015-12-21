with open("day_18_input.txt") as f:
    lines = f.readlines()

grid, temp,  count = [[0 for i in range(100)] for j in range(100)], [[0 for i in range(100)] for j in range(100)], 0

for line in lines:
    for i in range(len(line)):
        if(line[i] == '#'):
            grid[count][i] = 1
    count += 1

for x in range(100):
    for i in range(100):
        for j in range(100):
            temp[i][j] = grid[i][j]
    for i in range(100):
        for j in range(100):
            count = 0
            if(i > 0 and j > 0 and temp[i-1][j-1] == 1):
                count += 1
            if(i > 0 and temp[i-1][j] == 1):
                count += 1
            if(i > 0 and j < 99 and temp[i-1][j+1] == 1):
                count += 1
            if(j > 0 and temp[i][j-1] == 1):
                count += 1
            if(j < 99 and temp[i][j+1] == 1):
                count += 1
            if(i < 99 and j > 0 and temp[i+1][j-1] == 1):
                count += 1
            if(i < 99 and temp[i+1][j] == 1):
                count += 1
            if(i < 99 and j < 99 and temp[i+1][j+1] == 1):
                count += 1
            if(temp[i][j] == 1 and (count != 2 and count != 3)):
                grid[i][j] = 0
            if(temp[i][j] == 0 and count == 3):
                grid[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if(grid[i][j] == 1):
            count += 1
print count
