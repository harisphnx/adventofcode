with open("day_16_input.txt") as f:
    lines = f.readlines()

info_dict = {"children:": 3, "cats:": 7, "samoyeds:": 2, "pomeranians:": 3, "akitas:": 0, "vizslas:": 0, "goldfish:": 5, "trees:": 3, "cars:": 2, "perfumes:": 1}

for line in lines:
    name_val, count = {}, 0
    for i in range(2, 8, 2):
        name_val[(line.rstrip().split(' ')[i])] = int(line.rstrip().split(' ')[i+1][:len(line.rstrip().split(' ')[i+1]) - ((i/6)^1)])
    for name in name_val:
        if( (name == "cats:" or name == "trees:") and info_dict[name] < name_val[name]):
            count += 1
        elif( (name == "pomeranians:" or name == "goldfish:") and info_dict[name] > name_val[name]):
            count += 1
        elif((info_dict[name] == name_val[name]) and (name != "cats:" and name != "trees:" and name != "pomeranians:" and name != "goldfish:")):
            count += 1
    if(count == 3):
        print line.rstrip().split(' ')[0], line.rstrip().split(' ')[1]
