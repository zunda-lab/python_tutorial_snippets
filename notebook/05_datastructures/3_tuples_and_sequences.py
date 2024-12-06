t = 12345, 54321, 'hello!'
t[0]
# 12345

t
# (12345, 54321, 'hello!')

# タプルはネストできる
u = t, (1, 2, 3, 4, 5)
u
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# タプルは変更できない
t[0] = 88888
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-4-25494dd8d631> in <cell line: 2>()
      1 # タプルは変更できない
----> 2 t[0] = 88888
# TypeError: 'tuple' object does not support item assignment

# しかし、変更可能なオブジェクトを含むことはできる
v = ([1, 2, 3], [3, 2, 1])
v
# ([1, 2, 3], [3, 2, 1])

empty = ()
singleton = 'hello',    # <-- 後ろのコンマに注意
len(empty)
# 0

len(singleton)
# 1

singleton
# ('hello',)

x, y, z = t

x
# 12345

y
# 54321

z
# 'hello!'

