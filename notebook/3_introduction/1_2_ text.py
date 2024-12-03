'spam eggs'  # シングルクォート
# 'spam eggs'

"Paris rabbit got your back :)! Yay!"  # ダブルクォート
# 'Paris rabbit got your back :)! Yay!'

'1975'  # 引用符で囲まれた数字も文字列です
# '1975'

'doesn\'t'  # \'を使ってシングルクォートをエスケープします
# "doesn't"

"doesn't"  # または代わりにダブルクォートを使います
# "doesn't"

'"Yes," they said.'
# '"Yes," they said.'

"\"Yes,\" they said."
# '"Yes," they said.'

'"Isn\'t," they said.'
# '"Isn\'t," they said.'

s = 'First line. \nSecond line.'  # \n は改行を意味します
s  # print() を使わないと、特殊文字は文字列に含まれます
# 'First line. \nSecond line.'

print(s)  # print() を使うと、特殊文字が解釈されるので、\n は改行を生成します
# First line. 
# Second line.

print('C:\some\name')  # ここで \n は改行を意味します!
# C:\some
# ame

print(r'C:\some\name')  # 引用符の前に r があることに注意してください
# C:\some\name

print("""\
Usage: thingy [OPTIONS]
    -h Display this usage message
    -H hostname Hostname to connect to
""")
# Usage: thingy [OPTIONS]
#     -h Display this usage message
#     -H hostname Hostname to connect to
# 

# 3回 'un' を繰り返し、その後に 'ium' を付けます
3 * 'un' + 'ium'
# 'unununium'

'Py' 'thon'
# 'Python'

text = ('Put several strings within parentheses '
        'to have them joined together.')
text
# 'Put several strings within parentheses to have them joined together.'

prefix = 'Py'

prefix 'thon'  # 変数と文字列リテラルを連結することはできません
#   File "<ipython-input-18-e82a0defc0f8>", line 1
    prefix 'thon'  # 変数と文字列リテラルを連結することはできません
           ^
SyntaxError: invalid syntax

('un' * 3) 'ium'
#   File "<ipython-input-19-f4764cbe42a8>", line 1
    ('un' * 3) 'ium'
               ^
SyntaxError: invalid syntax

prefix + 'thon'
# 'Python'

word = 'Python'
word[0]  # 位置 0 の文字
# 'P'

word[5]  # 位置 5 の文
# 'n'

word[-1]  # 最後の文字
# 'n'

word[-2]  # 最後から2番目の文字
# 'o'

word[-6]
# 'P'

word[0:2]  # 位置 0 (含む) から 2 (含まない) までの文字
# 'Py'

word[2:5]  # 位置 2 (含む) から 5 (含まない) までの文字
# 'tho'

word[:2]  # 先頭から位置 2 (含まない) までの文字
# 'Py'

word[4:]  # 位置 4 (含む) から末尾までの文字
# 'on'

word[-2:]  # 最後から2番目 (含む) から末尾までの文字
# 'on'

word[:2] + word[2:]
# 'Python'

word[:4] + word[4:]
# 'Python'

word[42]  # 単語は6文字しかありません
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-33-fbaa00624d1d> in <cell line: 1>()
----> 1 word[42]  # 単語は6文字しかありません
# IndexError: string index out of range

word[4:42]
# 'on'

word[42:]
# ''

word[0] = 'J'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-36-91a956888ca7> in <cell line: 1>()
----> 1 word[0] = 'J'
# TypeError: 'str' object does not support item assignment

word[2:] = 'py'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-37-6488bbf78f5a> in <cell line: 1>()
----> 1 word[2:] = 'py'
# TypeError: 'str' object does not support item assignment

'J' + word[1:]
# 'Jython'

word[:2] + 'py'
# 'Pypy'

s = 'supercalifragilisticexpialidocious'
len(s)

