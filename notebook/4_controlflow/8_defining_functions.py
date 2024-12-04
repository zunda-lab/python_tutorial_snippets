def fib(n):    # write Fibonacci series less than n
    """nより小さいフィボナッチ数列を出力する"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 

fib
# <function __main__.fib(n)>

f = fib
f(100)
# 0 1 1 2 3 5 8 13 21 34 55 89 

fib(0)
print(fib(0))
# 
# 
# None

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

