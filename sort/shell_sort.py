"""
    shell sort
"""


def shell_sort(li):
    # calculate the h value, which is the hop value
    h = 1
    while h < len(li)-1:
        h = 2*h + 1

    for hop in range(h, 0, -int(h/2)):
        for to_be_inserted in range(hop, len(li)):
            if li[to_be_inserted] < li[to_be_inserted-hop]:
                li[to_be_inserted], li[to_be_inserted-hop] = li[to_be_inserted-hop], li[to_be_inserted]

    return li


print(shell_sort([0,-1,3,2,-9]))


