num, count = int(raw_input("")), 1

while(True):
    the_sum = 0
    for x in set(reduce(list.__add__, ([i, count//i] for i in range(1, int(count**0.5) + 1) if count % i == 0))):
        if( x*50 >= count):
            the_sum += x
    if(the_sum * 11 >= num):
        print count
        break
    count += 1
