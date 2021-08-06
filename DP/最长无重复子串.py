def unrepeated(li):
    if len(li) == 1:
        return 1
    if li == "":
        return 0

    max_length = 1
    literate_start = 0
    for i in range(len(li)):
        temp_max_length = 1
        for j in range(literate_start, i):
            if li[j] == li[i]:
                literate_start = i
                temp_max_length = 1
                break
            else:
                temp_max_length += 1

        if temp_max_length > max_length:
            max_length = temp_max_length

    return max_length


def unrepeated_lower_time_complexity(li):
    if len(li) == 1:
        return 1
    if li == "":
        return 0

    max_length = 1
    literate_start = 0
    occured = set()
    temp_max_length = 0
    for i in range(len(li)):
        if li[i] not in occured:
            occured.add(li[i])
            temp_max_length += 1
        else:
            occured.add(li[i])
            temp_max_length = 0

        if temp_max_length > max_length:
            max_length = temp_max_length

    return max_length

s = "abcccdef"
print(unrepeated(s))