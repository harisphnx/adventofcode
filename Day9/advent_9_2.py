from itertools import permutations

with open("day_9_input.txt") as f:
    routes = f.readlines()

route_mat, perms, ans, count = [[0 for i in range(8)] for i in range(8)], [''.join(p) for p in permutations('01234567')], -9999, 0

for i in range(8):
    for j in range(i+1, 8):
        route_mat[i][j] = int(routes[count].split(' ')[4])
        route_mat[j][i] = int(routes[count].split(' ')[4])
        count += 1

for perm in perms:
    temp = 0
    for j in range(len(perm)-1):
        temp += route_mat[int(perm[j])][int(perm[j+1])]
    if(temp > ans):
        ans = temp
print ans
