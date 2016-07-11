mylist = ['line 1','line 2','line 3']

f = open('written_to_text.txt','w')

lines_out = [line + '\n' for line in mylist]
f.writelines(lines_out)
f.close()
