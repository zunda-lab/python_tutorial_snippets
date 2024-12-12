try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
# Goodbye, world!
# ---------------------------------------------------------------------------
# KeyboardInterrupt                         Traceback (most recent call last)
# <ipython-input-1-ca8991ac7661> in <cell line: 1>()
      1 try:
----> 2     raise KeyboardInterrupt
      3 finally:
      4     print('Goodbye, world!')
# KeyboardInterrupt: 

def bool_return():
    try:
        return True
    finally:
        return False

bool_return()
# False

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
# result is 2.0
# executing finally clause

divide(2, 0)
# division by zero!
# executing finally clause

divide("2", "1")
# executing finally clause
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-5-3ad63cdb9b7d> in <cell line: 1>()
----> 1 divide("2", "1")
# <ipython-input-3-7495096d7580> in divide(x, y)
      1 def divide(x, y):
      2     try:
----> 3         result = x / y
      4     except ZeroDivisionError:
      5         print("division by zero!")
# TypeError: unsupported operand type(s) for /: 'str' and 'str'

