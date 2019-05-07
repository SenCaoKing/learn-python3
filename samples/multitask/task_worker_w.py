import time, sys, queue, random
from multiprocessing.managers import BaseManager

BaseManager.register('get_task')
BaseManager.register('get_result')

conn = BaseManager(address=('127.0.0.1', 5002), authkey=b'123')

try:
    conn.connect()
except:
    print('连接失败')
    sys.exit()

task = conn.get_task()
result = conn.get_result()

while not task.empty():
    n = task.get(timeout=1)
    print('run task %d' % n)
    sleeptime = random.randint(0, 3)
    time.sleep(sleeptime)
    rt = (n, sleeptime)
    result.put(rt)

if __name__=='__main__':
    pass
# run task 0
# run task 1
# run task 2
# run task 3
# run task 4
# run task 5
# run task 6
# run task 7
# run task 8
# run task 9
