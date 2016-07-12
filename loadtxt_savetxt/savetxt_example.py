from matplotlib.pyplot import *
from numpy import *

#fmt='%.18e', delimiter=' ', newline='\n', header=''

t = arange(0,1,0.01)
y1 = sin(2*pi*t)
y2 = cos(4*pi*t)

data = column_stack([t,y1,y2])
comments = ['line 1','line 2','line 3']
labels = ['t','y1','y2']

label_row = ','.join(labels)
myheader = '\n'.join(comments)
myheader += '\n'
myheader  += label_row

savetxt('savetxt_data_text.csv', data, delimiter=',', header=myheader)
