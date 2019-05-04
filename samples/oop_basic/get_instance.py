class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Animal):
    pass

a = Animal()
d = Dog()
h = Husky()

print('check a = Animal()...') # check a = Animal()...
print('isinstance(a, Animal) =', isinstance(a, Animal)) # isinstance(a, Animal) = True
print('isinstance(a, Dog) =', isinstance(a, Dog)) # isinstance(a, Dog) = False
print('isinstance(a, Husky) =', isinstance(a, Husky)) # isinstance(a, Husky) = False

print('check d = Dog()...') # check d = Dog()...
print('isinstance(d, Animal) =', isinstance(d, Animal)) # isinstance(d, Animal) = True
print('isinstance(d, Dog) =', isinstance(d, Dog)) # isinstance(d, Dog) = True
print('isinstance(d, Husky) =', isinstance(d, Husky)) # isinstance(d, Husky) = False

print('check h = Husky()...') # check h = Husky()...
print('isinstance(h, Animal) =', isinstance(h, Animal)) # isinstance(h, Animal) = True
print('isinstance(h, Dog) =', isinstance(h, Dog)) # isinstance(h, Dog) = False
print('isinstance(h, Husky) =', isinstance(h, Husky)) # isinstance(h, Husky) = True