import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000')) # 1000000 = 64
print('1010101 =', int2('1010101')) # 1010101 = 85