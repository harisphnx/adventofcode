containers, ans = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40], 0

for i in range(1048577):
    temp, count, val = bin(i)[2:], 0, 0
    while(len(temp) < 20):
        temp = "0" + temp
    for bit in temp:
        if(int(bit) == 1):
            val += cont[count]
        count += 1
    if(val == 150):
        ans += 1
print ans
