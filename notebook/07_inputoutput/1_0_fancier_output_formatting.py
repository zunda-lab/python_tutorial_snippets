year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
# 'Results of the 2016 Referendum'

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
# ' 42572654 YES votes  49.67%'

s = 'Hello, world.'
str(s)
# 'Hello, world.'

repr(s)
# "'Hello, world.'"

str(1/7)
# '0.14285714285714285'

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The value of x is 32.5, and y is 40000...

# repr()は、文字列に引用符とバックスラッシュを追加する
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# 'hello, world\n'

# repr()の引数は任意のPythonオブジェクト
repr((x, y, ('spam', 'eggs')))
# "(32.5, 40000, ('spam', 'eggs'))"

