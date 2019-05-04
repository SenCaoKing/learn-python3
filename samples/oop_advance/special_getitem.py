class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0]) # 1
print(f[5]) # 8
print(f[100]) # 573147844013817084101
print(f[0:5]) # [1, 1, 2, 3, 5]
print(f[:10]) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]