with open("day_7_input.txt") as f:
    commands = f.readlines()

gate_dict = {}
flag = 1

while(flag == 1):
    flag = 0
    for x in commands:
        temp = x.rstrip().split(" ")
        if( len(temp) == 3 ):                                                             #direct assignment
            if(temp[0] in gate_dict and temp[2] not in gate_dict):                          #through gate
                flag = 1
                gate_dict[temp[2]] = gate_dict[temp[0]]
            elif(ord(temp[0][0]) < 58 and temp[2] not in gate_dict):                        #through number
                flag = 1
                gate_dict[temp[2]] = int(temp[0])
        elif( len(temp) == 4 ):                                                           #not
            if(temp[1] in gate_dict and temp[3] not in gate_dict):                          #through gate
                flag = 1
                gate_dict[temp[3]] = ~gate_dict[temp[1]]
            elif(ord(temp[1][0]) < 58 and temp[3] not in gate_dict):                        #through number
                flag = 1
                gate_dict[temp[3]] = ~int(temp[1])
        elif( (temp[0] in gate_dict or ord(temp[0][0]) < 58) and (temp[2] in gate_dict or ord(temp[2][0]) < 58) and temp[4] not in gate_dict):
            flag = 1
            if(temp[0] in gate_dict):
                x = gate_dict[temp[0]]
            elif( ord(temp[0][0]) < 58):
                x = int(temp[0])
            if(temp[2] in gate_dict):
                y = gate_dict[temp[2]]
            elif( ord(temp[2][0]) < 58):
                y = int(temp[2])
            if(temp[1] == "AND"):
                gate_dict[temp[4]] = x & y
            if(temp[1] == "OR"):
                gate_dict[temp[4]] = x | y
            if(temp[1] == "LSHIFT"):
                gate_dict[temp[4]] = x << y
            if(temp[1] == "RSHIFT"):
                gate_dict[temp[4]] = x >> y
#print gate_dict['a']        
print gate_dict
