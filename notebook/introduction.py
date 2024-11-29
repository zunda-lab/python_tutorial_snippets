# これは最初のコメントです
spam = 1 # そしてこれは2番目のコメントです
# ... そして今は3番目!
text = "# これはコメントではありません。なぜなら引用符の中にあるからです。"

2 + 2
# 4

50 - 5*6
# 20

(50 - 5*6) / 4
# 5.0

8 / 5  # 除算は常に浮動小数点数を返します。
# 1.6

17 / 3  # 従来の除算は浮動小数点数を返します
# 5.666666666666667

17 // 3  # 切り捨て除算は小数部分を切り捨てます
# 5

17 % 3  # % 演算子は除算の剰余を返します
# 2

5 * 3 + 2  # 切り捨てられた商 * 除数 + 剰余
# 17

5 ** 2  # 5の2乗
# 25

2 ** 7  # 2の7乗
# 128

width = 20
height = 5 * 9
width * height
# 900

n  # 未定義の変数にアクセスしようとします
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-14-2232f5f156dc> in <cell line: 1>()
----> 1 n  # 未定義の変数にアクセスしようとします
# NameError: name 'n' is not defined

4 * 3.75 - 1
# 14.0

tax = 12.5 / 100
price = 100.50
price * tax
# 12.5625

price + _
# 113.0625

round(_, 2)
# 113.06

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
#   File "<ipython-input-45-e82a0defc0f8>", line 1
    prefix 'thon'  # 変数と文字列リテラルを連結することはできません
           ^
SyntaxError: invalid syntax

('un' * 3) 'ium'
#   File "<ipython-input-46-f4764cbe42a8>", line 1
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
# <ipython-input-61-fbaa00624d1d> in <cell line: 1>()
----> 1 word[42]  # 単語は6文字しかありません
# IndexError: string index out of range

word[4:42]
# 'on'

word[42:]
# ''

word[0] = 'J'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-66-91a956888ca7> in <cell line: 1>()
----> 1 word[0] = 'J'
# TypeError: 'str' object does not support item assignment

word[2:] = 'py'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-67-6488bbf78f5a> in <cell line: 1>()
----> 1 word[2:] = 'py'
# TypeError: 'str' object does not support item assignment

'J' + word[1:]
# 'Jython'

word[:2] + 'py'
# 'Pypy'

s = 'supercalifragilisticexpialidocious'
len(s)
# 34

squares = [1, 4, 9, 16]
squares
# [1, 4, 9, 16]

squares[0]  # インデックス指定は要素を返します
# 1

squares[-1]
# 16

squares[-3:]  # スライスは新しいリストを返します
# [4, 9, 16]

squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125] # ここに何か間違いがあります
4 ** 3  # 4の3乗は64であって、65ではありません!
# 64

cubes[3] = 64  # 間違った値を置き換えます
cubes
# [1, 8, 27, 64, 125]

cubes.append(216)  # 6の3乗を追加します
cubes.append(7 ** 3)  # そして7の3乗を追加します
cubes
# [1, 8, 27, 64, 125, 216, 343]

rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # それらは同じオブジェクトを参照します
# True

rgba.append("Alph")
rgb
# ['Red', 'Green', 'Blue', 'Alph']

correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
correct_rgba
# ['Red', 'Green', 'Blue', 'Alpha']

rgba
# ['Red', 'Green', 'Blue', 'Alph']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# いくつかの値を置き換えます
letters[2:5] = ['C', 'D', 'E']
letters
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# 今度はそれらを削除します
letters[2:5] = []
letters
# ['a', 'b', 'f', 'g']

# すべての要素を空のリストに置き換えることでリストをクリアします
letters[:] = []
letters
# []

letters = ['a', 'b', 'c', 'd']
len(letters)
# 4

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
# [['a', 'b', 'c'], [1, 2, 3]]

x[0]
# ['a', 'b', 'c']

x[0][1]
# 'b'

# フィボナッチ数列:
# 2つの要素の和が次の要素を定義します
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
# 0
# 1
# 1
# 2
# 3
# 5
# 8

i = 256*256
print('The value of i is', i)
# The value of i is 65536

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
