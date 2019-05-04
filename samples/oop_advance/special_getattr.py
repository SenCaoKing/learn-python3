class Student(object):

    def __init__(self):
        self.name = 'Sen'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name) # Sen
print(s.score) # 99
print(s.age()) # 25
# AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)