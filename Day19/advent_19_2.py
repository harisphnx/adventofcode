import re

with open("day_19_input.txt") as f:
    lines = f.readlines()

mol, the_list = lines[-1].rstrip(), []

for i in range(len(lines)-2):
    the_form = lines[i].rstrip().split(' ')
    temp_list = [m.start() for m in re.finditer(the_form[0], mol)]
    for pos in temp_list:
        temp_mol = mol[:pos] + the_form[2] + mol[pos+len(the_form[0]):]
        if(temp_mol not in the_list):
            the_list.append(temp_mol)

print len(the_list)
