
def fun(string):
    if len(string) <= 1:
        return True

    has_repeat = set()
    for i in range(len(set)):
        if string[i] not in has_repeat:
            has_repeat.add(string[i])
        else:
            return False
        
    return True
