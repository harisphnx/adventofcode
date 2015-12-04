with open("day_2_input.txt") as f:
    boxes = f.readlines()
ans = 0

def small(temp):
    temp.remove(max(temp))
    return temp[0] * temp[1]

'''
while(0):
    test = list()
    for i in range(3):
        test.append(int(raw_input("")))
    print small(test)
'''

for x in boxes:
    temp = [ int(i) for i in x.rstrip().split('x') ]
    #temp1 = x.rstrip().split('x')
    #temp = [int(temp1[0]), int(temp1[1]), int(temp1[2]) ]
    ans += ( (2*temp[0]*temp[1]) + (2*temp[1]*temp[2]) + (2*temp[2]*temp[0])) +  small(temp)

print ans
