from fibo import fib, fib2
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import *
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import fibo as fib
fib.fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import fib as fibonacci
fibonacci(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

import fibo

