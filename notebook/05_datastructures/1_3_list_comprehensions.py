squares = []
for x in range(10):
    squares.append(x**2)

squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x**2, range(10)))
squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = [x**2 for x in range(10)]
squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

vec = [-4, -2, 0, 2, 4]
# 値を2倍にした新しいリストを作成する
[x*2 for x in vec]
# [-8, -4, 0, 4, 8]

# リストをフィルタリングして負の数を除外する
[x for x in vec if x >= 0]
# [0, 2, 4]

# すべての要素に関数を適用する
[abs(x) for x in vec]
# [4, 2, 0, 2, 4]

# 各要素に対してメソッドを呼び出す
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit']

# (数値, 平方) のような2要素タプルのリストを作成する
[(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# タプルは括弧で囲む必要がある。そうしないとエラーが発生する。
[x, x**2 for x in range(6)]
#   File "<ipython-input-25-e04308bd5b51>", line 2
    [x, x**2 for x in range(6)]
     ^
SyntaxError: did you forget parentheses around the comprehension target?

# 2つの 'for' を持つリスト内包表記を使ってリストをフラット化する
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']

