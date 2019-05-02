s = 'Python - 中文'
print(s) # Python - 中文
b = s.encode('utf-8')
print(b) # b'Python - \xe4\xb8\xad\xe6\x96\x87'
print(b.decode('utf-8')) # Python - 中文