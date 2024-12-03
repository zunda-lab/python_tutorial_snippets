# 文字列計測:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
# cat 3
# window 6
# defenestrate 12

# コレクション作成
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# 方針:  コピーを反復
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# 方針:  新コレクション作成
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

