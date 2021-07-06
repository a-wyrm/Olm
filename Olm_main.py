from gtts import gTTS
import os
# language will be in English.
language = 'en'

# eventually, the program name will be user-entered
program_name = 'Olm_t.py'

# Eventually, this program will be able to tell the edits to a code
# and give the user the option of starting the TTS at the specific thing
# they edited

if (os.path.isfile('Olm_wf.txt') == True):
    os.remove('Olm_wf.txt')

# eventually, I will make an interface that will allow these properties
# to be turned off
program_t = True

with open(program_name,'r') as tts_file, open('Olm_wf.txt','a') as write_f:
    # Program line counter
    program_count = 1

    for line in tts_file:
        # NEXT THING TO IMPLEMENT:
        # IGNORE COMMENTS
        # LIST ARRAY PROPERTIES, LIST VARIABLE PROPERTIES
        if (program_t == True) and line != '\n':
            write_f.write(str(program_count) + '... ')
            program_count += 1
        # This is how we delay indents, we do this by tricking the tokenizer with "..."
        # this delays it just enough to make the program comprehendable
        if '\n' in line:
            line = ("... ") + line

        write_f.write(line)



tts_text = open('Olm_wf.txt', 'r').read().replace("\n", " ")
speech  = gTTS(text = str(tts_text), lang = language, slow = False)
  
# saving the converted audio in an mp3
speech.save("Olm_tts.mp3")
