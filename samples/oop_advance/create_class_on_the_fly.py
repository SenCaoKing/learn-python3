def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print('call h.hello():') # call h.hello():
h.hello() # Hello, world.
print('type(Hello) =', type(Hello)) # type(Hello) = <class 'type'>
print('type(h) =', type(h)) # type(h) = <class '__main__.Hello'>