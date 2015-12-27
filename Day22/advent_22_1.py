spells, min_mana = [[53, 1, 4, 0, 0, 0], [73, 1, 2, 2, 0, 0], [113, 6, 0, 0, 7, 0], [173, 6, 3, 0, 0, 0], [229, 5, 0, 0, 0, 101]], 9999

def play(spell, p_mana, p_hit, p_arm, s, p, r, b_hit, spent, min_mana):
    ####player turn
    #effect
    if(s > 0):
        p_arm = spells[2][4]
        s -= 1
    if(p > 0):
        b_hit -= spells[3][2]
        if(b_hit <= 0 and spent < min_mana):
            min_mana = spent
        p -= 1
    if(r > 0):
        p_mana += spells[4][5]
        r -= 1

    #check if same effect spell or not
    if((s > 0 and spell == 2) or (p > 0 and spell == 3) or (r > 0 and spell == 4) or b_hit <= 0):
        return min_mana

    p_mana -= spells[spell][0]
    spent += spells[spell][0]

    if(spell == 0):
        b_hit -= spells[spell][2]
    elif(spell == 1):
        b_hit -= spells[spell][2]
        p_hit += spells[spell][3]
    elif(spell == 2):
        s = spells[spell][1]
    elif(spell == 3):
        p = spells[spell][1]
    elif(spell == 4):
        r = spells[spell][1]

    ####boss turn
    #effect
    p_arm = 0
    if(s > 0):
        p_arm = spells[2][4]
        s -= 1
    if(p > 0):
        b_hit -= spells[3][2]
        p -= 1
    if(r > 0):
        p_mana += spells[4][5]
        r -= 1

    if(b_hit <= 0 and spent < min_mana):
        min_mana = spent

    p_hit -= (9 - p_arm)
    if(p_hit <= 0 or p_mana < 0 or spent > min_mana or b_hit <= 0):
        return min_mana

    ####recursion
    for i in range(5):
        min_mana = play(i, p_mana, p_hit, 0, s, p, r, b_hit, spent, min_mana)
    return min_mana

for i in range(5):
    min_mana = play(i, 500, 50, 0, 0, 0, 0, 58, 0, min_mana)
print min_mana
