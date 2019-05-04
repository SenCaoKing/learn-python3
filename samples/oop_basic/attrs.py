class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # hasattr(obj, 'x') = True
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # hasattr(obj, 'y') = False
setattr(obj, 'y', 19)
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # hasattr(obj, 'y') = True
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # getattr(obj, 'y') = 19
print('obj.y =', obj.y) # obj.y = 19

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404)) # getattr(obj, 'z') = 404

f = getattr(obj, 'power')
print(f()) # <bound method MyObject.power of <__main__.MyObject object at 0x00000254D7B74F60>>
print(f) # 81
