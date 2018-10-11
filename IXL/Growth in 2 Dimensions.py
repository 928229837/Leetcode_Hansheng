def two_d(n, input):
    x, y = [], []
    for i in input:
        a, b = i.split()
        print('a:'+a, 'b:'+b)
        x.append(int(a))
        y.append(int(b))
    return min(i for i in x)*min(j for j in y)





print(two_d(3, ["2 3", "3 7", "4 1"]))