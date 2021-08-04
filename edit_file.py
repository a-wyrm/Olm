import os
from difflib import Differ

edit_file = True

#if (os.path.isfile('Olm_wf.txt') == True) and edit_file == True:

# Olm_wf is already written, compare Olm_wf with the program file and find what's
# different

# if the line is equal to what's already in the Olm_wf file, do NOT copy it

# note: make it so temp_file is deleted first
# rename have tts voice over the temp file if option is selected


program_name = 'Olm_t.py'
starting_line = ""
with open(program_name, 'r') as tts_file, open('Olm_wf.txt', 'r') as Olm_f, open('temp_file.txt','a') as write_f:
    differ = Differ()

    for line in differ.compare(tts_file.readlines(), Olm_f.readlines()):
        if line.startswith("-"):
            starting_line = (line[2:])
            break
    tts_file.close()

    with open(program_name, 'r') as tts_file:
        for starting in tts_file:
            if starting_line in starting:
                write_f.write(starting_line)
                for starting in tts_file:
                    write_f.write(starting)
