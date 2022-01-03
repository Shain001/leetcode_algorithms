def check(target):
    if target == " " or target == "":
        return False

    sum = 0
    for i in range(len(target)):
        if target[i] == 'a':
            sum += 1

        elif target[i] == 'b':
            sum -= 1

        else:
            return False

        if sum < 0:
            return False

    return sum == 0


test1 = 'ab'
test2 = 'aabb'
test3 = 'abab'
test4 = 'aababb'
test5 = 'aaabbb'
test6 = 'aababb'
test7 = ''

test = [test1, test2, test3, test4, test5, test6, test7]
for i in range(len(test)):
    target = test[i]
    print(check(target))