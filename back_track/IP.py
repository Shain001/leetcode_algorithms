"""
2021/1/17
力扣93

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你不能重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

 

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
"""


# def ip_combination(nums):
#     def back_track(remained_num, tmep_part, num_of_part_remain, ip):
#
#         # terminate
#         if len(remained_num) == 0:
#             to_return.append(ip + tmep_part)
#             return
#
#         # check illegal characters
#         if not remained_num[0].isdigit():
#             to_return.clear()
#             return
#
#         if len(remained_num) > num_of_part_remain * 3:
#             return
#
#         if len(tmep_part) == 3:
#             # back_track(remained_num, "", num_of_part_remain - 1, ip + tmep_part+".")
#             return
#
#         if tmep_part != "" and int(tmep_part) > 255:
#             # back_track(remained_num+tmep_part[-1], "", num_of_part_remain-1, ip + tmep_part[:-1] + ".")
#             return
#
#         if len(tmep_part) >= 2 and tmep_part[0] == 0:
#             return
#
#
#
#
#     if len(nums) < 4:
#         return ""
#
#     to_return = []
#
#
#     return to_return


def ip_config(s):
    def back_track(remained_s, ip, ip_seg, count):

        # 剪枝条件
        if len(remained_s) > count * 3:
            return

        if not remained_s.isdigit():
            return

        if ip_seg != "" and int(ip_seg[0:-1]) > 255:
            return

        if len(ip_seg) >= 3 and ip_seg[0] == '0':
            return

        # 终止条件
        if count == 1:
            if int(remained_s) <= 255 and remained_s[0] != '0' or len(remained_s) == 1:
                ip += remained_s
                to_return.append(ip)
            return

        for i in range(1, 4):
            ip_seg = remained_s[0:i] + "."
            temp = ip + ip_seg
            back_track(remained_s[i:], temp, ip_seg, count - 1)

    if len(s) < 4 or len(s) > 12:
        return []

    to_return = []
    back_track(s, "", "", 4)
    return to_return


s = "9999999"
print(ip_config(s))
