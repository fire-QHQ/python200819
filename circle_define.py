def circle_area(x):
    a = x*x*3.14
    return a

def circle_circum(x):
    b = x*2*3.14
    return b

c = int(input('半徑?:'))
d = circle_area(c)
g = circle_circum(c)

print('面積:',d,'周長:',g)