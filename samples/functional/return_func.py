def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f) # <function lazy_sum.<locals>.sum at 0x000002AF34DC89D8>
print(f()) # 36
# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1()) # 9
print(f2()) # 9
print(f3()) # 9

# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1()) # 1
print(f2()) # 4
print(f3()) # 9