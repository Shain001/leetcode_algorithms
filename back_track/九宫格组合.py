"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

"""


def combination(arr):
    if arr == "":
        return None
    nums = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def back_track(combos, next_digit):
        if len(next_digit) == 0:
            result.append(combos)
        else:
            for ch in nums[next_digit[0]]:
                back_track(combos + ch, next_digit[1:])

    result = []
    back_track("", arr)
    return result


digits = "23"
print(combination(digits))