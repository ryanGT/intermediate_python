import os

topdir = '.'

for root, dirs, files in os.walk(topdir):
    if ".git" in root:
        continue
    print('root: %s' % root)

print('-'*20)

# quick abspath demo
absroot = os.path.abspath(root)
print('absroot: %s' % absroot)

print('\n'*2)
print('Part 2')
print('-'*20)

for root, dirs, files in os.walk(topdir):
    if ".git" in root:
        continue
    print('')#blank line
    print('root: %s' % root)
    if dirs:
        print('    dirs:')
        for curdir in dirs:
            print('    %s' % curdir)
        print('')#blank line
    if files:
        print('    files:')
        for curfile in files:
            print('    %s' % curfile)
            
    print('~'*15)
    
