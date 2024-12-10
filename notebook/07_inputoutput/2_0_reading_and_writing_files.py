f = open('workfile', 'w', encoding="utf-8")

with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# ファイルが自動的に閉じられていることを確認できます。
f.closed
# True

f.close()
f.read()
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-3-bf012af3c351> in <cell line: 2>()
      1 f.close()
----> 2 f.read()
# ValueError: I/O operation on closed file.

