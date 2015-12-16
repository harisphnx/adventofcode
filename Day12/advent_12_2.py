import json

dics, count =  json.load(open("day_12_input.txt")), 0

def rec_count(single_dic):
    global count
    if( isinstance(single_dic, int) ):
        count += single_dic
    if( isinstance(single_dic, list) ):
        for x in single_dic:
            rec_count(x)
    if( isinstance(single_dic, dict) ):
        if( "red" in single_dic.values() ):
            return
        for x in single_dic:
            rec_count(single_dic[x])

rec_count(dics)

print count
