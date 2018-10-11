def ang_diff(a, b):
    ans = []
    for l in range(len(a)):
        i = a[l]
        j = b[l]
        print(i, j)
        if len(i) != len(j):
            ans.append(-1)
            continue
        for i_c in i:
            index = j.find(i_c)
            if index != -1:
                j = j[:index]+j[index+1:]
        ans.append(len(j))
    return ans






print(ang_diff(['a','jk','abb','mn','abc'],
               ['bb','kj','bbc','op','def']))