from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L)) # ['Credit', 'Zoo', 'about', 'bob']
print(sorted(L, key=str.lower)) # ['about', 'bob', 'Credit', 'Zoo']

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0))) # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)
print(sorted(students, key=lambda t: t[1])) # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
print(sorted(students, key=itemgetter(1), reverse=True)) # [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]