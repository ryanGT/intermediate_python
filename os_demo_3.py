import os

os.system('ifconfig')

print('\n')
print('='*20)
print('\n')

dir1 = os.getcwd()#get current working directory
print('dir1: %s' % dir1)


temp_name = 'temp_dir'

# delete the temp dir if it exists:
if os.path.exists(temp_name):
    os.rmdir(temp_name)
    
os.mkdir(temp_name)# throws an error if the directory already exists

os.chdir(temp_name)
dir2 = os.getcwd()
print('dir2: %s' % dir2)

os.chdir(dir1)
final_dir = os.getcwd()
print('final_dir: %s' % final_dir)
