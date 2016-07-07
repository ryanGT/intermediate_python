import os

# os module
# =========

# os.path
# +++++++++++++

goodname = 'text_file.txt'
badname = 'non_existent.csv'

good_bool = os.path.exists(goodname)
bad_bool = os.path.exists(badname)

print('good_bool: %s' % good_bool)
print('bad_bool: %s' % bad_bool)

print('-'*20)

folder = 'files'
fn = 'Krauss_Ryan_quiz_2_b.py'
krauss_path  = os.path.join(folder, fn)
print('krauss_path: %s' % krauss_path)
krauss_bool = os.path.exists(krauss_path)
print('krauss_bool: %s' % krauss_bool)

print('-'*20)

mypath = 'myfolder/myfilename.py'
folder2, fn2 = os.path.split(mypath)

print('folder2: %s' % folder2)
print('fn2: %s' % fn2)

fno, ext = os.path.splitext(fn2)
print('fno: %s' % fno)
print('ext: %s' % ext)
