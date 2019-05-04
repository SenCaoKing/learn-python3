from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

print('day1 =', day1) # day1 = Weekday.Mon
print('Weekday.Tue =', Weekday.Thu) # Weekday.Tue = Weekday.Thu
print('Weekday[\'Tue\'] =', Weekday['Tue']) # Weekday['Tue'] = Weekday.Tue
print('Weekday.Tue.value =', Weekday.Thu.value) # Weekday.Tue.value = 4
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon) # day1 == Weekday.Mon ? True
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue) # day1 == Weekday.Tue ? False
print('day1 == Weekday(1) ?', day1 == Weekday(1)) # day1 == Weekday(1) ? True

for name, member in Weekday.__members__.items():
    print(name, '=>', member)
# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12
