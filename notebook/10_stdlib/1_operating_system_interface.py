import os
os.getcwd() # 現在のワーキングディレクトリを返す
# 'C:\\Python313'
os.chdir('/server/accesslogs') # 現在のワーキングディレクトリを変更する
os.system('mkdir today') # システムシェルでmkdirコマンドを実行する
# 0

import os
dir(os)
# <returns a list of all module functions>
help(os)
# <returns an extensive manual page created from the module's docstrings>

import shutil
shutil.copyfile('data.db', 'archive.db')
# 'archive.db'
shutil.move('/build/executables', 'installdir')
# 'installdir'

