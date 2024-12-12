try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     raise TypeError('bad type')
# TypeError: bad type
# Add some information
# Add some more information

def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 1, in <module>
#   |     raise ExceptionGroup('We have some problems', excs)
#   | ExceptionGroup: We have some problems (3 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | Traceback (most recent call last):
#     |   File "<stdin>", line 3, in <module>
#     |     f()
#     |     ~^^
#     |   File "<stdin>", line 2, in f
#     |     raise OSError('operation failed')
#     | OSError: operation failed
#     | Happened in Iteration 1
#     +---------------- 2 ----------------
#     | Traceback (most recent call last):
#     |   File "<stdin>", line 3, in <module>
#     |     f()
#     |     ~^^
#     |   File "<stdin>", line 2, in f
#     |     raise OSError('operation failed')
#     | OSError: operation failed
#     | Happened in Iteration 2
#     +---------------- 3 ----------------
#     | Traceback (most recent call last):
#     |   File "<stdin>", line 3, in <module>
#     |     f()
#     |     ~^^
#     |   File "<stdin>", line 2, in f
#     |     raise OSError('operation failed')
#     | OSError: operation failed
#     | Happened in Iteration 3
#     +------------------------------------

