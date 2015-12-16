def check(s):
    if( 'i' in s or 'o' in s or 'l' in s):
        return 0
    count = 0
    flag = 0
    char = ""
    for i in range(len(s)-1):
        if(s[i] == s[i+1] and s[i] not in char):
            count += 1
            char += s[i]
    for i in range(len(s)-2):
        if(s[i] == chr(ord(s[i+1])-1) and s[i+1] == chr(ord(s[i+2])-1)):
            flag = 1
    if(count >= 2 and flag == 1):
        return 1
    else:
        return 0

def gen(s):
    temp = ""
    if( (ord(s[len(s)-1]) - 96) == 26 ):
        temp += gen(s[:len(s)-1]) + "a"
    else:
        return (s[:len(s)-1] + chr(ord(s[len(s)-1])+1))
    return temp

test = 0
string = "vzbxkghb"

while(test == 0):
    string = gen(string)
    if(check(string)):
        test = 1
print string
