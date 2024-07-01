# def test_func(compute):
#     result = compute(1,2)
#     print(result)
#
# def compute(x,y):
#     return x + y
#
# test_func(compute)
#
#
# def test_func(compute):
#     result = compute(1,2)
#     print(result)
#
# test_func(lambda x,y:x + y)

from datetime import datetime

a = datetime.today()
print(a)
print(a.year)
print(a.month)
print(a.day)
from datetime import date
a = date(2017,3,1)
b = date(2017,3,15)
print(a.__eq__(b))
print(a.__ge__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__lt__(b))
print(a.__ne__(b))

print(a.__sub__(b))
print(a.__rsub__(b))

print(a.__format__('%Y-%m-%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__str__())

from datetime import time
t=time(12,20,55,590)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print(t.__format__('%H:%M:%S'))

b = datetime.now()
print(b)
print(b.date())
print(b.time())
print('-'*50)
from datetime import timedelta
b1 = b+timedelta(days=1)
print(b1)

b2 = b + timedelta(days=10 , hours=23,seconds=500)
print(b2)
print('-'*50)





