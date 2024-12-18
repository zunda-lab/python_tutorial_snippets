sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

import sound.effects.echo

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects import echo

echo.echofilter(input, output, delay=0.7, atten=4)

from sound.effects.echo import echofilter

echofilter(input, output, delay=0.7, atten=4)

__all__ = ["echo", "surround", "reverse"]

__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'

import sound.effects.echo
import sound.effects.surround
from sound.effects import *

from . import echo
from .. import formats
from ..filters import equalizer

