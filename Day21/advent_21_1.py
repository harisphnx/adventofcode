weapon, armor, ring, min_gold = [[8,4], [10,5], [25,6], [40,7], [74,8]], [[13,1], [31,2], [53,3], [75,4], [102,5], [0, 0]], [[25,1,0], [50,2,0], [100,3,0], [20,0,1], [40,0,2], [80,0,3]], 9999

def play(i, j, x, p_hit, min_gold):
    b_hit, b_dam, b_arm, p_dam, gold, p_arm = 104, 8, 1, weapon[i][1], weapon[i][0], armor[j][1]
    gold += armor[j][0]

    for k in range(len(x)):
        if(x[k] == str(1)):
            p_dam += ring[k][1]
            p_arm += ring[k][2]
            gold += ring[k][0]
    while(p_hit > 0 and b_hit > 0):
        if( (p_dam - b_arm) < 0):
            b_hit -= 1
        else:
            b_hit -= (p_dam - b_arm)
        if(b_hit <= 0 and gold < min_gold):
            return gold
        if( (b_dam - p_arm) < 0):
            p_hit -= 1
        else:
            p_hit -= (b_dam - p_arm)
    return min_gold

for i in range(len(weapon)):
    for j in range(len(armor)):
        for x in range(64):
            if(bin(x).count('1') < 3):
                min_gold = play(i, j, (bin(x)[2:].zfill(6)), 100, min_gold)
print min_gold
