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
program_com = False
program_var = True
slow = False

with open(program_name,'r') as tts_file, open('Olm_wf.txt','a') as write_f:
    # Program line counter
    program_count = 1

    for line in tts_file:

        if (program_com == False):
            # Ignore comments
            if(line[0] == '#'):
                pass

            # Ignore inline comments
            line = line.partition('#')[0]

        #List variable properties
        for char in line:
            if char is '=' and line[line.find('=')+1] != '=':
                findvar = -1
                findend = 1

                while line[line.find(char) + findvar] == ' ':
                    findvar -= 1
                foundvar = line[line.find(char) + findvar]

                findingcount = line[line.find(char) + findend]
                while findingcount == ' ' or findingcount == "'":
                    findend += 1
                    findingcount = line[line.find(char) + findend]
                foundend = line[line.find(char) + findend]

                # In case variable names are longer than 1 character...
                #...
                
                typevar = ""
                if(foundend.isalpha()):
                    typevar = "string"
                elif(foundend.isnumeric()):
                    typevar = "integer"

                line = line.replace(str(foundvar), typevar + " " + foundvar)
                    

        # NEXT THING TO IMPLEMENT:
        # LIST ARRAY PROPERTIES
        if (program_t == True) and line != '\n':
            write_f.write(str(program_count) + '... ')
            program_count += 1
        
        # This is how we delay indents, we do this by tricking the tokenizer with "..."
        # this delays it just enough to make the program comprehendable
        addellipses = True
        try:
            line[-2]
        except IndexError:
            addellipses = False
        if addellipses:
            line = line + ("... ")
        write_f.write(line)



tts_text = open('Olm_wf.txt', 'r').read().replace("\n", " ")
speech  = gTTS(text = str(tts_text), lang = language, slow = slow)
  
# saving the converted audio in an mp3
speech.save("Olm_tts.mp3")
