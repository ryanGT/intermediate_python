import time
from numpy.random import rand

def read_data():
    fake_data = int(rand()*100)
    return fake_data


N = 3
fmt = '%H:%M:%S%p %m/%d/%y'
row_fmt = '%s,%s'#csv row
out_list = []

for i in range(N):
    time_stamp = time.strftime(fmt)
    cur_data = read_data()
    cur_row = row_fmt % (time_stamp, cur_data)
    print(cur_row)
    out_list.append(cur_row)
    time.sleep(2)#waith 2 seconds


label_row = 'Time Stamp,Fake Data'

# prepend label_row to out_list
# Note that lists can be added together to make longer lists
out_list = [label_row] + out_list

# add newline characters
out2 = [item + '\n' for item in out_list]

f = open('strftime_out_data.csv','w')
f.writelines(out2)
f.close()

