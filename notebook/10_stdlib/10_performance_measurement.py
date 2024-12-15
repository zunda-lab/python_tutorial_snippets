from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.04956585000000757

Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.03391886699999702

