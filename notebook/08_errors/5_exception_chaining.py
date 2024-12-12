try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
# ---------------------------------------------------------------------------
# FileNotFoundError                         Traceback (most recent call last)
# <ipython-input-1-c2e47e28551a> in <cell line: 1>()
      1 try:
----> 2     open("database.sqlite")
      3 except OSError:
# FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'
# 
During handling of the above exception, another exception occurred:
# RuntimeError                              Traceback (most recent call last)
# <ipython-input-1-c2e47e28551a> in <cell line: 1>()
      2     open("database.sqlite")
      3 except OSError:
----> 4     raise RuntimeError("unable to handle error")
# RuntimeError: unable to handle error

# exc must be exception instance or None.
raise RuntimeError from exc

def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
# ---------------------------------------------------------------------------
# ConnectionError                           Traceback (most recent call last)
# <ipython-input-2-d7352cebcbcd> in <cell line: 4>()
      4 try:
----> 5     func()
      6 except ConnectionError as exc:
# <ipython-input-2-d7352cebcbcd> in func()
      1 def func():
----> 2     raise ConnectionError
      3 
# ConnectionError: 
# 
The above exception was the direct cause of the following exception:
# RuntimeError                              Traceback (most recent call last)
# <ipython-input-2-d7352cebcbcd> in <cell line: 4>()
      5     func()
      6 except ConnectionError as exc:
----> 7     raise RuntimeError('Failed to open database') from exc
# RuntimeError: Failed to open database

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
# ---------------------------------------------------------------------------
# RuntimeError                              Traceback (most recent call last)
# <ipython-input-3-df1beb6f71b4> in <cell line: 1>()
      2     open('database.sqlite')
      3 except OSError:
----> 4     raise RuntimeError from None
# RuntimeError: 

