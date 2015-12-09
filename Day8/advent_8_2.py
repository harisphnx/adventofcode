with open("day_8_input.txt") as f:
    strings = f.readlines()

count = 0
for x in strings:
    temp = x.strip()
    count += 2 + temp.count('"') + temp.count('\\')
print count
