# 练习题：利用os模块编写一个能实现dir -l输出的程序
# dir -l 用于Unix系统下打印目录的详细信息，每行输出格式为: 访问权限，硬链接数，文件所有者，文件组，文件大小，修改时间和文件名
# Windows 下是直接调用dir命令即可，每行输出格式为: 显示目录或文件的大小，修改时间，文件名
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('       Size  Last Modified    Name')
print('       --------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
    #  Size  Last Modified    Name
    # --------------------------------------
    # 608  2019-05-05 17:11  do_bytesio.py
    # 420  2019-05-05 17:43  do_dir.py
    # 446  2019-05-05 17:04  do_stringio.py
    # 463  2019-05-05 16:51  with_file.py