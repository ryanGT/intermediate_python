import glob, os, shutil


def contains_numbers(string_in):
    for i in range(10):
        if str(i) in string_in:
            # we found at least one number, exit
            return True
    # if the code made it to here, we didn't find any numbers
    return False


def contains_g_thru_z(string_in):
    """I cheated and googled how to get a list of letters.  See this
    thread on stackoverflow:

    http://stackoverflow.com/questions/16060899/alphabet-range-python

    string.ascii_lowercase is all lowercase letters a-z, we want g-z
    """
    import string
    g_thru_z = string.ascii_lowercase[6:]

    for letter in g_thru_z:
        if letter in string_in:
            return True
    return False


def check_one(first_part):
    """Check to see if first part is a hexidecimal stamp from
    blackboard or a true first or last name.  hexidecimal stamps would
    be long (probably 32 characters) and contain only 0-9 and a-f
    (lowercase).  True names would probably be shorter and shouldn't
    contain any numbers."""
    N = len(first_part)
    is_long = N > 25
    has_numbers = contains_numbers(first_part)
    has_g_thru_z = contains_g_thru_z(first_part)
    if (is_long and has_numbers):
        return True
    elif has_g_thru_z:
        return False
    else:
        raise ValueError, "not sure about this: " + first_part
    

folder = 'files'
pat = os.path.join(folder,'*.py')
all_files = glob.glob(pat)

bool_list = []
big_list = []

for curfile in all_files:
    folder, fn = os.path.split(curfile)
    first, rest = fn.split('_',1)
    cur_bool = check_one(first)
    bool_list.append(cur_bool)
    
    if cur_bool:
        outname = rest
    else:
        outname = fn

    big_list.append([fn, outname, cur_bool])


just_test = 0

for old_name, new_name, cur_bool in big_list:
    if cur_bool:
        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)
        print('%s --> %s' % (old_path, new_path))
        if not just_test:
            shutil.move(old_path, new_path)
