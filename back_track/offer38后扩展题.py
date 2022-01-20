"""
2022/1/18
offer2 P 218, 第38题后的扩展题
"""

def combination(s):
    def back_track(count, path):
        if count == 0:
            to_return.append(path[:])
            return

        for i in range(len(s)):
            if used[i] is False:
                used[i] = True
                if count == len(s):
                    to_return.append(s[i])
                path.append(s[i])
                back_track(count-1, path)
                used[i] = False
                path.pop()

    if len(s) <= 2:
        return [s]

    to_return = []
    used = [False] * len(s)
    back_track(len(s), [])
    return to_return

s = "abc"
print(combination(s))