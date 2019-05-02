# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {
    'Sen': 125,
    'Bob': 78,
    'Tracy': 98
}
print('d[\'Sen\'] =', d['Sen']) # d['Sen'] = 125
print('d[\'Bob\'] =', d['Bob']) # d['Bob'] = 78
print('d[\'Tracy\'] =', d['Tracy']) # d['Tracy'] = 98
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1)) # d.get('Thomas', -1) = -1