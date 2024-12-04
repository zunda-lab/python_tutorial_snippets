def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
# 2

standard_arg(arg=2)
# 2

pos_only_arg(1)
# 1

pos_only_arg(arg=1)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-5-434db44f4ff9> in <cell line: 1>()
----> 1 pos_only_arg(arg=1)
# TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

kwd_only_arg(3)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-6-896c53ef896c> in <cell line: 1>()
----> 1 kwd_only_arg(3)
# TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

kwd_only_arg(arg=3)
# 3

combined_example(1, 2, 3)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-8-037a05a37207> in <cell line: 1>()
----> 1 combined_example(1, 2, 3)
# TypeError: combined_example() takes 2 positional arguments but 3 were given

combined_example(1, 2, kwd_only=3)
# 1 2 3

combined_example(1, standard=2, kwd_only=3)
# 1 2 3

combined_example(pos_only=1, standard=2, kwd_only=3)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-11-a0fe0f8338e9> in <cell line: 1>()
----> 1 combined_example(pos_only=1, standard=2, kwd_only=3)
# TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

def foo(name, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-13-1e719af70668> in <cell line: 1>()
----> 1 foo(1, **{'name': 2})
# TypeError: foo() got multiple values for argument 'name'

def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
# True

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

