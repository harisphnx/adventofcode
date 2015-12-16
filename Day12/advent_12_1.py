import re

with open("day_12_input.txt") as f:
    num_list, count = re.findall("[-\d]+", f.readline().rstrip()), 0

for num in num_list:
    count += int(num)

print count
