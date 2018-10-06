import collections

a = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
d = collections.OrderedDict(a)
d['b'] =10

d['a'] =10

print(d)
d.popitem(last=False)
print(d)
d['xx'] = 10
print(d)
d.pop('apple')
print(d)