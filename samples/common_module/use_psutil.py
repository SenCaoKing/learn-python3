import psutil
print(psutil.cpu_count()) # CPU逻辑数量: 8

print(psutil.cpu_count(logical=False)) # CPU物理核心: 4
# 4说明是4核超线程，8则是8新非超线程

# 统计CPU的用户 / 系统 / 空闲时间：
print(psutil.cpu_times())
# scputimes(user=115879.953125, system=74888.62500000047, idle=2525043.8906249995, interrupt=4145.59375, dpc=1756.203125)

# 实现类似top命令的CPU使用率：
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))
# [16.7, 12.5, 37.5, 20.3, 28.1, 10.9, 21.9, 21.9]
# [9.2, 12.5, 10.9, 3.1, 4.7, 0.0, 32.8, 1.6]
# [16.9, 10.9, 9.4, 3.1, 3.1, 0.0, 10.9, 9.4]
# [10.9, 12.5, 15.6, 9.4, 9.4, 7.8, 23.4, 9.4]
# [18.8, 10.9, 14.1, 15.6, 10.9, 12.5, 18.8, 14.1]
# [18.5, 18.5, 33.8, 9.2, 21.5, 6.2, 29.2, 13.8]
# [26.6, 14.1, 18.8, 12.5, 25.0, 9.4, 9.4, 35.9]
# [13.4, 12.3, 7.8, 14.3, 7.8, 3.1, 7.8, 14.1]
# [25.4, 12.5, 15.6, 9.2, 7.8, 9.2, 20.0, 10.8]
# [12.3, 32.8, 10.9, 31.2, 28.1, 1.6, 17.2, 9.4]

# 获取内存信息：
print(psutil.virtual_memory())
# svmem(total=8445181952, available=2817306624, percent=66.6, used=5627875328, free=2817306624)
print(psutil.swap_memory())
# sswap(total=15156068352, used=9642242048, free=5513826304, percent=63.6, sin=0, sout=0)

# 获取磁盘信息：
print(psutil.disk_partitions()) # 磁盘分区信息
# [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='G:\\', mountpoint='G:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='H:\\', mountpoint='H:\\', fstype='CDFS', opts='ro,cdrom')]
print(psutil.disk_usage('/')) # 磁盘使用情况
# sdiskusage(total=214747312128, used=3053576192, free=211693735936, percent=1.4)
print(psutil.disk_io_counters()) # 磁盘IO
# sdiskio(read_count=4326745, write_count=5177262, read_bytes=126987448832, write_bytes=125021871104, read_time=14241, write_time=6315)

# 获取网络信息：
print(psutil.net_io_counters()) # 获取网络读写字节/包的个数
# snetio(bytes_sent=37107030, bytes_recv=699074295, packets_sent=404627, packets_recv=608784, errin=0, errout=0, dropin=0, dropout=0)
print(psutil.net_if_addrs()) # 获取网络接口信息

print(psutil.net_if_stats()) # 获取网络接口状态

print(psutil.net_connections()) # 获取当前网络连接信息

# 获取进程信息
print(psutil.pids()) # 所有进程ID

p = psutil.Process(580) # 获取指定进程ID=3780
print(p.name()) # 进程名称

print(p.exe()) # 进程exe路径

print(p.cwd()) # 进程工作目录

print(p.cmdline()) # 进程启动的命令行

print(p.ppid()) # 父进程ID

print(p.parent()) # 父进程

print(p.children()) # 子进程列表

print(p.status()) # 进程状态

print(p.username()) # 进程用户名

print(p.create_time()) # 进程创建时间

print(p.terminal()) # 进程终端

print(p.cpu_times()) # 进程使用的CPU时间

print(p.memory_info()) # 进程使用的内存

print(p.open_files()) # 进程打开的文件

print(p.connections()) # 进程相关网络连接

print(p.num_threads()) # 进程的线程数量

print(p.threads()) # 所有线程信息

print(p.environ()) # 进程环境变量

print(p.terminate()) # 结束进程