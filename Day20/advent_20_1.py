num, count = int(raw_input("")), 1

while(True):
    if(sum(set(reduce(list.__add__, ([i, count//i] for i in range(1, int(count**0.5) + 1) if count % i == 0)))) * 10 >= num):
        print count
        break
    count += 1
