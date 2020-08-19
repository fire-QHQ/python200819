a = []
r = []
b = 0
c = 100
d = 0

for i in range(5):
    e = int(input('成績:'))
    w = input('人名:')
    a.append(e)
    r.append(w)
    
    if e > b:
        b = e
        wb = w
    if e < c:
        c = e
        wc = w
    d = d + e

f = d/len(a)
print('平均:',f)
print('總分:',d)
print('最高分:',b)
print('最高分的人:',wb)
print('最低分:',c)
print('最低分的人:',wc)