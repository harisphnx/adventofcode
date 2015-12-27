letters, i = [1, 0], 0

with open("day_23_input.txt") as f:
    lines = f.readlines()

while(i < len(lines)):
    comm = lines[i].rstrip().split(' ')
    if(comm[0] == "inc"):
        letters[ord(comm[1])-97] += 1
    elif(comm[0] == "tpl"):
        letters[ord(comm[1])-97] *= 3
    elif(comm[0] == "hlf"):
        letters[ord(comm[1])-97] /= 2
    elif(comm[0] == "jmp"):
        exec('i = i' + str(comm[1][0]) + 'int(comm[1][1:]) - 1')
    elif(comm[0] == "jie"):
        if((comm[1][0] == "a" and letters[0] % 2 == 0) or (comm[1][0] == "b" and letters[1] % 2 == 0)):
            exec('i = i' + str(comm[2][0]) + 'int(comm[2][1:]) - 1')
    elif(comm[0] == "jio"):
        if((comm[1][0] == "a" and letters[0] == 1) or (comm[1][0] == "b" and letters[1] == 1)):
            exec('i = i' + str(comm[2][0]) + 'int(comm[2][1:]) - 1')
    i += 1
print letters
