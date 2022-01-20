"""
2022/1/17
start review backtracking
"""
def string_combination(string):
    def back_track(used, path):
        if False not in used:
            to_return.append(path[:])
            return

        for i in range(len(string)):
            if used[i] is False:
                used[i] = True
                path.append(string[i])
                back_track(used, path)
                used[i] = False
                path.pop()

    if len(string) == 0:
        return []

    to_return = []
    used = [False] * len(string)
    back_track(used, [])
    return to_return


print(string_combination("abc"))
