# 自定义函数
import math

# 求绝对值函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 求坐标函数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n) # 20

x, y = move(100, 100, 60, math.pi / 6)
print(x, y) # 151.96152422706632 70.0

my_abs('123') # TypeError: bad operand type