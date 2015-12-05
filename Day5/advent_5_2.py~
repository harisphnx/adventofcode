with open("advent_5_input.txt") as f:
    strings = f.readlines()
nice = 0

for x in strings:
    t1 = t2 = 0
    for i in range(len(x)-1):
        if(t1 == 0 and x[i:i+2] in x[i+2:]):
            t1 = 1
        if(t2 == 0 and i < len(x)-2 and x[i] == x[i+2]):
            t2 = 1
    if(t1 == 1 and t2 == 1):
        nice += 1
print nice
