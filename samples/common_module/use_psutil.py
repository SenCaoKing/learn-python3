import psutil
print(psutil.cpu_count()) # CPU逻辑数量: 8

print(psutil.cpu_count(logical=False)) # CPU物理核心: 4
# 4说明是4核超线程，8则是8新非超线程

print(psutil.cpu_times())

# 实现类似top命令的CPU使用率：
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息：
print(psutil.virtual_memory())

# 获取磁盘信息：
print(psutil.disk_partitions()) # 磁盘分区信息