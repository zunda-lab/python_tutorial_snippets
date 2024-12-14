class Dog:

    kind = 'canine'         # 全インスタンスで共有されるクラス変数

    def __init__(self, name):
        self.name = name    # インスタンスごとに固有のインスタンス変数

d = Dog('Fido')
e = Dog('Buddy')

d.kind                  # すべての犬で共有
# 'canine'

e.kind                  # すべての犬で共有
# 'canine'

d.name                  # d 固有
# 'Fido'

e.name                  # e 固有
# 'Buddy'

class Dog:

    tricks = []             # クラス変数の間違った使用

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # 意図せず すべての犬で共有
# ['roll over', 'play dead']

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # 犬ごとに新しい空リストを作る

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

d.tricks
# ['roll over']

e.tricks
# ['play dead']

