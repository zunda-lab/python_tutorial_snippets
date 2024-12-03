squares = [1, 4, 9, 16, 25]
squares
# [1, 4, 9, 16, 25]

squares[0]  # インデックス指定は要素を返します
# 1

squares[-1]
# 25

squares[-3:]  # スライスは新しいリストを返します
# [9, 16, 25]

squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

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

