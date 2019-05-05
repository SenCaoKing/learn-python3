from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...') # open for read...
    print(s) # 今天是 2019-05-05

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...') # open as binary for read...
    print(s) # b'\xbd\xf1\xcc\xec\xca\xc7 2019-05-05'