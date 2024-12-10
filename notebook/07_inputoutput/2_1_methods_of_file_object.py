with open('workfile', 'w', encoding="utf-8") as f:
    f.write('This is the entire file.\n')

f = open('workfile', encoding="utf-8")

f.read()
# 'This is the entire file.\n'

f.read()
# ''

f.close()

with open('workfile', 'w', encoding="utf-8") as f:
    f.write('This is the first line of the file.\n')
    f.write('Second line of the file\n')

f = open('workfile', encoding="utf-8")

f.readline()
# 'This is the first line of the file.\n'

f.readline()
# 'Second line of the file\n'

f.readline()
# ''

f.seek(0)
# 0

for line in f:
    print(line, end='')
# This is the first line of the file.
# Second line of the file

f.close()

f = open('workfile', 'w', encoding="utf-8")

f.write('This is a test\n')
# 15

value = ('the answer', 42)
s = str(value)  # タプルを文字列に変換する
f.write(s)
# 18

f.close()

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
# 16

f.seek(5)      # ファイルの6バイト目に移動する
# 5

f.read(1)
# b'5'

f.seek(-3, 2)  # 末尾の3バイト前に移動する
# 30

f.read(1)
# b'4'

f.close()

