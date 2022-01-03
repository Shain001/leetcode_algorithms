def tem(M, N):
    m_bin = list(bin(M)[2:])
    n_bin = list(bin(N)[2:])
    stack = []
    result = 0
    while len(m_bin) != 0 or len(n_bin) != 0:
        m = m_bin.pop(-1) if len(m_bin) != 0 else 0
        n = n_bin.pop(-1) if len(n_bin) != 0 else 0
        if m != n:
            stack.append(1)
        else:
            stack.append(0)

    i = 0
    while len(stack) != 0:
        result += stack.pop(0) * 2**i
        i += 1

    return result


print(tem(12,21))