def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 0 / n

def main():
    foo('0')

main() # AssertionError: n is zero!