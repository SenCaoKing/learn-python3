from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
# Parent process 4284.
# Waiting for all subprocesses done...
# Run task 0 (13072)...
# Run task 1 (3976)...
# Run task 2 (16460)...
# Run task 3 (672)...
# Task 3 runs 0.83 seconds.
# Run task 4 (672)...
# Task 0 runs 1.70 seconds.
# Task 1 runs 2.14 seconds.
# Task 2 runs 2.93 seconds.
# Task 4 runs 2.63 seconds.
# All subprocesses done.