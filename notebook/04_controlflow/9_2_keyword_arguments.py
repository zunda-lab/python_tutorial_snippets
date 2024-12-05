def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
# -- This parrot wouldn't voom if you put 1000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

parrot(voltage=1000)                                  # 1 keyword argument
# -- This parrot wouldn't voom if you put 1000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !

parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# -- This parrot wouldn't jump if you put a million volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's bereft of life !

parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
# -- This parrot wouldn't voom if you put a thousand volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's pushing up the daisies !

parrot()                     # required argument missing
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-8-9db1978cc13c> in <cell line: 1>()
----> 1 parrot()                     # required argument missing
# TypeError: parrot() missing 1 required positional argument: 'voltage'

parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#   File "<ipython-input-9-b18b24da62fc>", line 1
    parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
                              ^
SyntaxError: positional argument follows keyword argument

parrot(110, voltage=220)     # duplicate value for the same argument
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-10-be58d87c4290> in <cell line: 1>()
----> 1 parrot(110, voltage=220)     # duplicate value for the same argument
# TypeError: parrot() got multiple values for argument 'voltage'

parrot(actor='John Cleese')  # unknown keyword argument
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-11-a52dad5fe6e7> in <cell line: 1>()
----> 1 parrot(actor='John Cleese')  # unknown keyword argument
# TypeError: parrot() got an unexpected keyword argument 'actor'

def function(a):
    pass

function(0, a=0)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-12-0658d145b8a6> in <cell line: 4>()
      2     pass
      3 
----> 4 function(0, a=0)
# TypeError: function() got multiple values for argument 'a'

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch

