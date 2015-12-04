with open("day_2_input.txt") as f:
    boxes = f.readlines()
ans = 0

def small(temp):
    temp.remove(max(temp))
    return temp[0] * temp[1]

for x in boxes:
    temp = [ int(i) for i in x.rstrip().split('x') ]
    ans += ( (2*temp[0]*temp[1]) + (2*temp[1]*temp[2]) + (2*temp[2]*temp[0])) +  small(temp)

print ans
