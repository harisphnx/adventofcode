import re, random, copy

with open("day_19_input.txt") as f:
    lines = f.readlines()

mol, min_subs, the_dict, check_list = lines[-1].rstrip(), 9999, {}, []

for i in range(len(lines)-2):
    if lines[i].rstrip().split(' ')[2] not in the_dict:
        the_dict[lines[i].rstrip().split(' ')[2]] = lines[i].rstrip().split(' ')[0]

while(True):
    the_mol, the_list, flag, subs = copy.deepcopy(mol), [], 0, 0

    while(len(the_list) > 0 or flag == 0):
        for x in the_dict:
            if x in the_mol and x not in the_list:
                the_list.insert(i, x)

        temp, flag = random.randint(0, len(the_list)-1), 1
        while(the_list[temp] in the_mol):
            the_mol = the_mol.replace(the_list[temp], the_dict[the_list[temp]], 1)
            subs += 1
        the_list.pop(temp)

    if( the_mol == "e" and subs < min_subs):
        min_subs = subs
        print min_subs, "\n"
