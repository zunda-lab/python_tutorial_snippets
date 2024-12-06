basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 重複が削除されていることを示す
# {'pear', 'orange', 'banana', 'apple'}

'orange' in basket                 # 高速なメンバーシップテスト
# True

'crabgrass' in basket
# False

# 2つの単語の一意の文字に対する集合演算のデモ
a = set('abracadabra')
b = set('alacazam')
a                                  # a の一意の文字
# {'a', 'b', 'c', 'd', 'r'}

a - b                              # a にはあるが b にはない文字
# {'b', 'd', 'r'}

a | b                              # a または b または両方の文字
# {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}

a & b                              # a と b の両方に存在する文字
# {'a', 'c'}

a ^ b                              # a または b にはあるが両方にはない文字
# {'b', 'd', 'l', 'm', 'r', 'z'}

a = {x for x in 'abracadabra' if x not in 'abc'}
a
# {'d', 'r'}

