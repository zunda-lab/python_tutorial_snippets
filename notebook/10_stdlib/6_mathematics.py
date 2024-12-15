import math
math.cos(math.pi / 4)
# 0.7071067811865476

math.log(1024, 2)
# 10.0

import random
random.choice(['apple', 'pear', 'banana'])
# 'banana'

random.sample(range(100), 10)   # sampling without replacement
# [50, 14, 18, 11, 76, 36, 82, 92, 2, 9]

random.random()    # random float from the interval [0.0, 1.0)
# 0.9267376113241099

random.randrange(6)    # random integer chosen from range(6)
# 4

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
# 1.6071428571428572

statistics.median(data)
# 1.25

statistics.variance(data)
# 1.3720238095238095

