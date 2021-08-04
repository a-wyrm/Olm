import os
from difflib import Differ

starting_line = ""
def find_line(program_name):
    with open(program_name, 'r') as tts_file, open('temp_file.txt', 'r') as Olm_f:
        differ = Differ()
        for line in differ.compare(tts_file.readlines(), Olm_f.readlines()):
            if line.startswith("-"):
                globals()['starting_line']= (line[2:])
                break
        tts_file.close()
    return(starting_line)

if __name__ == '__main__':
    find_line(program_name)
