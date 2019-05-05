import pickle

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)
print(data) # b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'

reborn = pickle.loads(data)
print(reborn) # {'name': 'Bob', 'age': 20, 'score': 88}