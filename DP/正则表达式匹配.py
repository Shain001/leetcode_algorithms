def is_match(s: str, p: str):
    """
        此题重点在于理解：
        （1） dp二位数组的每一个格子代表的意义为： ”字符串中的前i为与pattern中的前j位是否匹配“。
        （2） 在填满dp数组的过程中， 填格子的顺序为 从左到右从上到下。 也即 依次加入一个字符串中的新字符， 然后把当前字符串片段与整个pattern逐位比较， 判断当前
            字符串片段能够匹配到pattern中的第几位为止。
        （3） 对于*号的处理：
            首先， * 号的状态可分为两种， 即为0与不为0：
            为0时， 相当于pattern中丢弃两位， 那么只要判断 f[i][j-2]是否为True即可， 也即相当于判断： 当前字符串片段是否符合 前j-2个pattern
            不为0时， 难点在于 *的值可能为 1，2，3，...
            但由于我们的字符串片段是逐次加入一个新的字符， 那么只需判断当前字符串片段的末尾字符是否等于*号前的字符即可。
            如果等于， 且加入新字符之前的字符串片段也是符合pattern的 （类似回文字符串的感觉）， 那么就是True。
            这就解决了*的值的问题。
    :param s:
    :param p:
    :return:
    """
    m, n = len(s), len(p)

    def matches(i: int, j: int) -> bool:
        if i == 0:
            return False
        if p[j - 1] == '.':
            return True
        return s[i - 1] == p[j - 1]

    f = [[False] * (n + 1) for _ in range(m + 1)]
    f[0][0] = True
    for i in range(m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                f[i][j] |= f[i][j - 2]  # 先把* 当成0 判断， 此时当前格子T/F与否，取决于 P 前移两位之前的部分与S是否匹配。
                # 这句if作用： 因为此时Pattern 被指向的字符为 *, 所以判断 * 之前的一位字符与当前指向的字符串中字符是否相等。
                # 如果相等的话，此时把字符串的i 往前移1位， j不变。 这代表着判断 字符串的不包含新加入的当前字符是否符合当前包含进来的pattern。
                # 这就解决了 * 的值有个能是重复1个或多个的问题。
                if matches(i, j - 1):
                    f[i][j] |= f[i - 1][j]
            else:
                if matches(i, j):
                    # 此处， 即 当前位如果相等了， 那么指针（包括现在指针指向的值） 之前字符是否符合与否就相当于 “两个指针” 都前移1位是否符合。
                    # 类似于判断回文字符串时， 新的两个字符进来， 如果这两个字符相等的话， 那么字符串整体是否是回文串就取决于进来新字符之前的字符串是否是回文字符串
                    f[i][j] |= f[i - 1][j - 1]
    return f[m][n]



s = "aa"
p = "a"


def is_match_rewrite(string, pattern):
    def is_valid(i, j):
        if i == 0:
            return False
        if pattern[j - 1] == ".":
            return True
        return string[i - 1] == pattern[j - 1]

    lines = len(string) + 1
    cols = len(pattern) + 1

    dp = [[False] * cols for _ in range(lines)]

    # 前0位字符 与 前0位pattern 匹配， 即空与空匹配
    dp[0][0] = True

    # i, j 为 dp的横纵坐标, i, j 对应string， pattern 中的index 为 i-1， j-1
    # 外层循环: 每次从字符串中取一个新的字符
    for i in range(lines):
        # 内层循环， 没取一个新字符， 则与前j位pattern对比是否匹配
        # 每取一个新的pattern， 又分为两种情况： * 或 非*
        # 若为*， 又分为两种情况： *为0， 或非0
        for j in range(1, cols):
            if pattern[j - 1] == "*":
                # 先假设 * 为0， 则：
                dp[i][j] = dp[i][j - 2]
                # 在假设 * 不为0, 则此时，只有*前的字符等于字符串中最后一个字符才有可能匹配
                if is_valid(i, j - 1):
                    # 取或的作用为不影响 假设*为0 得到的结果
                    dp[i][j] = dp[i][j] | dp[i - 1][j]

            else:
                if is_valid(i, j):
                    dp[i][j] = dp[i - 1][j - 1]

    return dp[-1][-1]


f = is_match_rewrite(s, p)
print(f)
