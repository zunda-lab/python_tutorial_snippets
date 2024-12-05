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
# <ipython-input-12-2232f5f156dc> in <cell line: 1>()
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
