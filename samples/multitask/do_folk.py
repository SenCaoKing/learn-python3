import os

print('Process (%s) start ...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.