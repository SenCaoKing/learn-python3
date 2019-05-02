# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1)) # fact(1) = 1
print('fact(5) =', fact(5)) # fact(5) = 120
print('fact(10) =', fact(10)) # fact(10) = 3628800

# 利用递归函数移动汉诺塔：
def move(n, a, b, c):
    if n == 1:
        print('move', a, '--->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
# move A ---> B
# move A ---> C
# move B ---> C
# move A ---> B
# move C ---> A
# move C ---> B
# move A ---> B
# move A ---> C
# move B ---> C
# move B ---> A
# move C ---> A
# move B ---> C
# move A ---> B
# move A ---> C
# move B ---> C