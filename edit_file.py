import os
edit_file = True

#if (os.path.isfile('Olm_wf.txt') == True) and edit_file == True:

# Olm_wf is already written, compare Olm_wf with the program file and find what's
# different

# if the line is equal to what's already in the Olm_wf file, do NOT copy it

# note: make it so temp_file is deleted first
# rename have tts voice over the temp file if option is selected

program_name = 'Olm_t.py'
with open(program_name,'r') as tts_file, open('Olm_wf.txt', 'r') as Olm_f, open('temp_file.txt','a') as write_f:
    for olm_line in Olm_f:
        for line in tts_file:
            if line != olm_line:
                write_f.write(line)
            break