def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # Hi! => greeting='Hi', args=()
hello('Hi', 'Sarah') # Hi, Sarah! => greeting='Hi', args=('Sarah')
hello('Hello', 'Sen', 'Bob', 'Adam') # Hello, Sen, Bob, Adam! => greeting='Hello', args=('Sen', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # Hello, Bart, Lisa! => greeting='Hello', args=('Bart', 'Lisa')