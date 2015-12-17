containers, ans, min_cont = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40], 0, 9999

for i in range(1048577):
    temp, count, val, cont_count = bin(i)[2:], 0, 0, 0
    while(len(temp) < 20):
        temp = "0" + temp
    for bit in temp:
        if(int(bit) == 1):
            val += containers[count]
            cont_count += 1
        count += 1
    if(val == 150):
        if(cont_count == min_cont):
            ans += 1
        if(cont_count < min_cont):
            min_cont = cont_count
            ans = 1
print ans
