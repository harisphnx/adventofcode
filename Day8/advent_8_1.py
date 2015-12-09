with open("day_8_input.txt") as f:
    strings = f.readlines()

count = 0
for x in strings:
    temp = x.strip()
    count += temp.count('\\\\')
    temp = temp.replace("\\\\", "$")
    count += 2 + temp.count('\\"') + (3 * temp.count('\\x'))
print count
