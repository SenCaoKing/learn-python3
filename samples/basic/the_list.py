# Python内置的一种数据类型就是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Sen', 'Bob', 'Tracy']
print('classmates =', classmates) # classmates = ['Sen', 'Bob', 'Tracy']
print('len(classmates) =', len(classmates)) # len(classmates) = 3
print('classmates[0] =', classmates[0]) # classmates[0] = Sen
print('classmates[1] =', classmates[1]) # classmates[1] = Bob
print('classmates[2] =', classmates[2]) # classmates[2] = Tracy
print('classmates[-1] =', classmates[-1]) # classmates[-1] = Tracy
classmates.pop()
print('classmates =', classmates) # classmates = ['Sen', 'Bob']

classmates[1] = 'Lucy'
print(classmates) # ['Sen', 'Lucy']

