# フィボナッチ数列:
# 2つの要素の和が次の要素を定義します
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
# 0
# 1
# 1
# 2
# 3
# 5
# 8

i = 256*256
print('The value of i is', i)
# The value of i is 65536

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
