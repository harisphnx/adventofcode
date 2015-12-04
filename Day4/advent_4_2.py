import hashlib

for i in range(100000000):
    if( hashlib.md5("yzbqklnj" + str(i)).hexdigest()[0:6] == "000000"):
        break
print i
