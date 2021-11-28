"""
给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/buddy-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Solution:

模拟
根据题意进行模拟即可，搞清楚什么情况下两者为「亲密字符」：

当 ss 与 goalgoal 长度 或 词频不同，必然不为亲密字符；
当「ss 与 goalgoal 不同的字符数量为 2（能够相互交换）」或「ss 与 goalgoal 不同的字符数量为 0，但同时 ss 中有出现数量超过 2 的字符（能够相互交换）」时，两者必然为亲密字符。

作者：AC_OIer
链接：https://leetcode-cn.com/problems/buddy-strings/solution/gong-shui-san-xie-jian-dan-zi-fu-chuan-m-q056/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

时间复杂度： 两个for + constant = O(n) ==> n is length of list
space complexity: O(C) == > C is 26; used by the Alpha counting list
"""


def buddy_string(target, source):
    # if length is different, return false
    lt = len(target)
    ls = len(source)
    if lt != ls:
        return False

    # 如果连个字符串符合条件， 则必然两个条件：
    # 1. 数组长度相等
    # 2. 且所有字符出现频率相同； 如 aaavc, aaacv
    # 如果符合条件1&2， 则：
    #    要么两个字符串相同index上字符不同的次数为2， 要么为0（此时即两个字符串完全相同）但字符串中有重复字符（否则无法互换）
    # 进而：
    # 依次比较两个数组的每一个字符，如果不同的次数为2， 则必然符合条件； 如 aavac, aaacv; 不同次数为3， 不符合 (事实上符合条件的两个字符串，不同次数非0即2)
    # 3. 如果不同次数为0； 则意味着这两个字符串完全相同， 此时有两种情况：
    # a. 字符串中没有重复的字符： abcdef --> 则无法互换符合条件
    # b. 字符串中有重复的字符： aabcdef ==> aabcdef 符合条件

    count_different = 0
    count_char_t = [0] * 26
    count_char_s = [0] * 26

    for i in range(0, lt):
        # 统计词频
        char_t_alpha = ord(target[i]) - ord('a')
        char_s_alpha = ord(source[i]) - ord('a')
        count_char_s[char_s_alpha] += 1
        count_char_t[char_t_alpha] += 1

        # 统计不同字符的个数
        if target[i] != source[i]:
            count_different += 1
            if count_different > 2:
                return False

    if count_different == 1:
        return False

    has_repeat = False

    # 此时，不同次数要么0要么2
    # 比较词频，以及查看是否有重复字符
    for i in range(0, 26):
        if count_char_t[i] != count_char_s[i]:
            return False
        if count_char_s[i] > 1:
            has_repeat = True

    # 至此，词频以相同，则只需判断different是0且has_repeat否， 或者different是否为2
    return count_different == 2 or has_repeat





