def read_and_strip_text_file(pathin):
    """Read a text file into a list and then strip off the newlines
    and other white space."""
    f = open(pathin, 'r')
    all_lines = f.readlines()
    f.close()
    clean_lines = [line.rstrip() for line in all_lines]
    return clean_lines



