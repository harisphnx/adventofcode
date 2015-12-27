import itertools, copy, operator

weights, total, min_mul, got = [1, 2, 3, 5, 7, 13 ,17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113], sum([1, 2, 3, 5, 7, 13 ,17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])/3, 999999999999999999999999, 0

def part_present(check_list, all_list, part):
    new_list = copy.deepcopy(all_list)
    for w in check_list:
        new_list.remove(w)

    for i in range(1, len(new_list)/part):
        temp_list = []

        for x in itertools.combinations(new_list, i):
            temp_list.append(x)
        for x in temp_list:
            if(sum(x) == total):
                return 1
    return 0

for i in range(1,8):
    if(got == 1):
        break
    list_2 = []
    for x in itertools.combinations(weights, i):
        list_2.append(x)

    for x in list_2:
        if(sum(x) == total and part_present(x, weights, 2) and reduce(operator.mul, x, 1) < min_mul):
            got, min_mul = 1, reduce(operator.mul, x, 1)
print min_mul
