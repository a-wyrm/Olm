from gtts import gTTS
import os
# language will be in English.
language = 'en'

# eventually, the program name will be user-entered
program_name = 'Olm_t.py'

if (os.path.isfile('Olm_wf.txt') == True):
    os.remove('Olm_wf.txt')

with open(program_name,'r') as tts_file, open('Olm_wf.txt','a') as write_f:
    
    for line in tts_file:
        # NEXT THING TO IMPLEMENT:
        # PROGRAM LINE COUNTER, IGNORE COMMENTS
        # LIST ARRAY PROPERTIES, LIST VARIABLE PROPERTIES
        # eventually, I will make an interface that will allow these properties to be
        # turned off
        # Find a way to delay indents
        write_f.write(line)



tts_text = open('Olm_wf.txt', 'r').read().replace("\n", " ")
speech  = gTTS(text = str(tts_text), lang = language, slow = False)
  
# saving the converted audio in an mp3
speech.save("Olm_tts.mp3")
