with open("day_2_input.txt") as f:
    boxes = f.readlines()
ans = 0

for line in boxes:
    a, b, c = sorted([int(x) for x in line.split('x')])
    ans += (a * b * c) + (2*a + 2*b)

print ans
