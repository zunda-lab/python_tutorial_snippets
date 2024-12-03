for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

list(range(5, 10))
# [5, 6, 7, 8, 9]

list(range(0, 10, 3))
# [0, 3, 6, 9]

list(range(-10, -100, -30))
# [-10, -40, -70]

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

range(10)
# range(0, 10)

sum(range(4))  # 0 + 1 + 2 + 3
# 6

