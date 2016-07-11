from matplotlib.pyplot import *
from numpy import *

import datetime
import text_utils

fn = 'strptime_example_data.csv'
clean_lines = text_utils.read_and_strip_text_file(fn)

date_strs = []
temps = []
date_objs = []
fmt = '%m/%d/%y'

for line in clean_lines[1:]:
    curdate, curtemp = line.split(',')
    curtemp = float(curtemp.strip())
    date_strs.append(curdate)
    temps.append(curtemp)
    cur_obj = datetime.datetime.strptime(curdate, fmt)
    date_objs.append(cur_obj)

d0 = date_objs[0]

deltas = [item-d0 for item in date_objs]
days = [item.days for item in deltas]

figure(1)
clf()
plot(days, temps, 'ro')
xticks(days, date_strs)

figure(2)
clf()
plot(days, temps, 'ro')
xlabels = [item.strftime('%m/%d') for item in date_objs]
xticks(days, xlabels)
ylim([0,100])
ylabel('Daily High Temperature')
xlabel('Date')

show()
    
