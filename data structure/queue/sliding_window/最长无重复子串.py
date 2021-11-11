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


def use_sliding_window(nums):
    window = []
    max_length = 1
    for i in range(len(nums)):
        if nums[i] not in window:
            window.append(nums[i])
        else:
            while nums[i] in window:
                window.pop(0)
            window.append(nums[i])
        max_length = max(max_length, len(window))
    return max_length



s = "abcccdef"
print(use_sliding_window(s))