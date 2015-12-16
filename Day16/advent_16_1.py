with open("day_16_input.txt") as f:
    lines = f.readlines()

info_dict = {"children:": 3, "cats:": 7, "samoyeds:": 2, "pomeranians:": 3, "akitas:": 0, "vizslas:": 0, "goldfish:": 5, "trees:": 3, "cars:": 2, "perfumes:": 1}

for line in lines:
    val1 = int(line.rstrip().split(' ')[3][:len(line.rstrip().split(' ')[3])-1])
    val2 = int(line.rstrip().split(' ')[5][:len(line.rstrip().split(' ')[5])-1])
    val3 =  int(line.rstrip().split(' ')[7][:len(line.rstrip().split(' ')[7])])
    if(info_dict[line.rstrip().split(' ')[2]] == val1 and  info_dict[line.rstrip().split(' ')[4]] == val2 and info_dict[line.rstrip().split(' ')[6]] == val3):
        print line.rstrip().split(' ')[0], line.rstrip().split(' ')[1]
