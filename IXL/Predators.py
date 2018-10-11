# 3. species 分group
# ex.
# input
# 3
# [-1, 0, 1]
# ------------
# 表示
# 3種species
# 這3種相對應的predator [-1, 0, 1]
# species 0 沒有predator (-1表示沒有predator)
# species 1 的predator 是species 0
#
# species 2 的predator 是species 1 (且因為1的predator 是 0 所以 species 2 有indirect predator 0)
#
#
#
# 之後把species分群 群的規定是每個species 只能分別放在一個group  且在這個group裡面的物種不會跟其direct or indirect predator放在一起
# 找出能符合上述條件的最少group


def predators(l):
    res = []
    temp = []
    length = len(l)
    indices = [i for i, x in enumerate(l) if x == -1]
    length -= len(indices)
    res.append(indices)
    while length:
        for num in res[-1]:
            temp.extend([i for i, x in enumerate(l) if x == num])
        res.append(temp)
        length -= len(temp)
        temp = []
    return res


a = [1, -1, 3, -1, 1, 3, 2, 0]

print(predators(a))





