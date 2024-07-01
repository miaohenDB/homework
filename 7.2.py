from datetime import timedelta
from datetime import time
from datetime import date
x = date(2004,6,16)
y = date(2024,6,2)
z = date(2024,6,16)
print(y.__sub__(x))
print(y.__rsub__(z))
