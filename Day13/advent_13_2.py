from itertools import permutations

with open("day_13_input.txt") as f:
    happiness = f.readlines()

happiness_mat, perms, g_l, ans, count = [[0 for i in range(9)] for i in range(9)], [''.join(p) for p in permutations('012345678')],{"gain":1,"lose":-1}, -9999, 0

for i in range(8):
    for j in range(8):
        if( i != j ):
            happiness_mat[i][j] = int(happiness[count].split(' ')[3]) * g_l[happiness[count].split(' ')[2]]
            count += 1

for perm in perms:
    temp = 0
    for j in range(-1, len(perm)-1):
        temp += happiness_mat[int(perm[j])][int(perm[j+1])] + happiness_mat[int(perm[j+1])][int(perm[j])]
    if(temp > ans):
        ans = temp
print ans
