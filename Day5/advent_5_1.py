with open("advent_5_input.txt") as f:
    strings = f.readlines()

vowels, str_restr, nice = ['a', 'e', 'i', 'o', 'u'], ["ab", "cd", "pq", "xy"], 0

for x in strings:
    vow_test = test = 0
    for s in str_restr:
        if s in x:
            test = 2
    for i in range(len(x)-1):
        if(test != 2 and vow_test < 3 and x[i] in vowels):
            vow_test += 1
        if(test != 2 and test != 1 and i > 0 and x[i-1] == x[i]):
            test = 1
    if(test == 1 and vow_test >= 3):
        nice += 1

print nice
