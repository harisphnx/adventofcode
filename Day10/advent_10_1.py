string, iterations = "1113222113", 1

while(iterations <= 40):
    temp, i = "", 0
    while( i < len(string)):
        count = 1
        while( i < len(string)-1 and string[i] == string[i+1]):
            count += 1
            i += 1
        temp += str(count) + str(string[i])
        i += 1

    string = temp
    iterations += 1
print len(string)
