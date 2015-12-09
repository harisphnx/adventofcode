with open("day_2_input.txt") as f:
    boxes = f.readlines()
ans = 0

for line in boxes:
    a, b, c = sorted([int(x) for x in line.split('x')])
    ans += 2*(a*b + b*c + a*c) + a*b

print ans
