filename = 'text_file.txt'

f = open(filename, 'r')
all_lines = f.readlines()#get all lines of the text file as a list;
                         #note that each line ends with \n or \r or
                         #whatever depending on how it was created

f.close()# do this as soon as you are done reading so you don't forget

# use .strip() and an implied for loop to clean white space
clean_lines = [line.strip() for line in all_lines]

# the implied for loop is the same as this longer code:
clean_lines2 = []

for line in all_lines:
    out = line.strip()
    clean_lines2.append(out)


# these lines could be placed in a helper function in a text utilities
# module and then easily imported when needed.

import text_utils
clean_lines3 = text_utils.read_and_strip_text_file(filename)

