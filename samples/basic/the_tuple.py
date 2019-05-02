# Python内置的另一种有序列表叫元组：tuple。tuple和list非常相似，但是tuple一旦初始化就不能修改
classmates = ('Sen', 'Bob', 'Tracy')
print('classmates =', classmates) # classmates = ('Sen', 'Bob', 'Tracy')
print('len(classmates) =', len(classmates)) # len(classmates) = 3
print('classmates[0] =', classmates[0]) # classmates[0] = Sen
print('classmates[1] =', classmates[1]) # classmates[1] = Bob
print('classmates[2] =', classmates[2]) # classmates[2] = Tracy
print('classmates[-1] =', classmates[-1]) # classmates[-1] = Tracy

# cannot modify tuple:
classmates[0] = 'Adam' # TypeError: 'tuple' object does not support item assignment