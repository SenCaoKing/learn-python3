# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s1 = set([1, 1, 2, 2, 3, 3])
print(s1) # {1, 2, 3}
s2 = set([2, 3 ,4])
print(s1 & s2) # {2, 3}
print(s1 | s2) # {1, 2, 3, 4}