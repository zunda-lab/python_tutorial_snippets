for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

s = 'abc'
it = iter(s)
it
# <str_iterator at 0x7bc9be20e5c0>

next(it)
# 'a'

next(it)
# 'b'

next(it)
# 'c'

next(it)
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-5-bc1ab118995a> in <cell line: 1>()
----> 1 next(it)
# StopIteration: 

class Reverse:
    """シーケンスを後ろからまわるイテレータ."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
# <__main__.Reverse at 0x7bc9be20ddb0>

for char in rev:
    print(char)
# m
# a
# p
# s

