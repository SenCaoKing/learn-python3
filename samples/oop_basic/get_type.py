# type()

print('type(123) =', type(123)) # type(123) = <class 'int'>
print('type(\'123\') =', type('123')) # type('123') = <class 'str'>
print('type(None) =', type(None)) # type(None) = <class 'NoneType'>
print('type(abs) =', type(abs)) # type(abs) = <class 'builtin_function_or_method'>

import types

print('type(\'abc\')==str?', type('abc')==str) # type('abc')==str? True