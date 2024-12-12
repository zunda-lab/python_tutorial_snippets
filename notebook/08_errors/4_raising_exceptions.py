raise NameError('HiThere')
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-1-72c183edb298> in <cell line: 1>()
----> 1 raise NameError('HiThere')
# NameError: HiThere

raise ValueError  # shorthand for 'raise ValueError()'

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
# An exception flew by!
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-2-bf6ef4926f8c> in <cell line: 1>()
      1 try:
----> 2     raise NameError('HiThere')
      3 except NameError:
      4     print('An exception flew by!')
      5     raise
# NameError: HiThere

