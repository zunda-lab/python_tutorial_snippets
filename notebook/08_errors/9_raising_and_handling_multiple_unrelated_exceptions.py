def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 1, in <module>
#   |     f()
#   |     ~^^
#   |   File "<stdin>", line 3, in f
#   |     raise ExceptionGroup('there were problems', excs)
#   | ExceptionGroup: there were problems (2 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | OSError: error 1
#     +---------------- 2 ----------------
#     | SystemError: error 2
#     +------------------------------------

try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')
# caught <class 'ExceptionGroup'>: e

def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
# There were OSErrors
# There were SystemErrors
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 2, in <module>
#   |     f()
#   |     ~^^
#   |   File "<stdin>", line 2, in f
#   |     raise ExceptionGroup(
#   |     ...<12 lines>...
#   |     )
#   | ExceptionGroup: group1 (1 sub-exception)
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------

excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)

