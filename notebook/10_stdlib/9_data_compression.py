import zlib
s = b'witch which has which witches wrist watch'
len(s)
# 41

t = zlib.compress(s)
len(t)
# 37

zlib.decompress(t)
# b'witch which has which witches wrist watch'

zlib.crc32(s)
# 226805979

