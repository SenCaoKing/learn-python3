import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data) # JSON Data is a str: {"name": "Bob", "age": 20, "score": 88}
reborn = json.loads(data)
print(reborn) # {'name': 'Bob', 'age': 20, 'score': 88}

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s %s %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data) # Dump Student: {"name": "Bob", "age": 20, "score": 88}
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild) # Student object (Bob 20 88)