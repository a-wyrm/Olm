from gtts import gTTS
import os
from edit_file import *

ef = True

def maketext(program_name, program_t, program_com, program_var, ef):
    with open(program_name,'r') as tts_file, open('Olm_wf.txt','a') as write_f:
        print(find_line(program_name))
        
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
            if (program_var):
                for char in line:
                    if char is '=' and line[line.find('=')+1] != '=':
                        findvar = -1
                        findend = 1

                        # In case variable names are longer than 1 character...
                        while line[line.find(char) + findvar] == ' ':
                            findvar -= 1
                        foundvar = line[0:line.find(char) + findvar]
                        if foundvar == "":
                            foundvar = line[0:line.find(char) + -1]

                        # Find the end
                        findingcount = line[line.find(char) + findend]
                        char_bool = False
                        while findingcount == ' ' or findingcount == "'" or findingcount == '"':
                            if findingcount == "'":
                                char_bool = True

                            findend += 1
                            findingcount = line[line.find(char) + findend]

                        foundend = line[line.find(char) + findend]
                        typevar = ""
                        array_l = ""
                        
                        # LIST ARRAY PROPERTIES
                        arraycheck = False
                        if foundend == '[':
                            convert_ar = eval(line[line.find(foundend):len(line)])
                            array_l = str(len(convert_ar))
            
                            foundend = line[line.find(char) + findend + 1]
                            arraycheck = True

                        if(char_bool):
                            typevar = "character"
                        elif(foundend.isalpha()):
                            typevar = "string"
                        elif(foundend.isnumeric()):
                            typevar = "integer"
                        elif(foundend == '{'):
                            typevar = "dictionary"


                        if(arraycheck):
                            string_c = " array of length " + array_l + " "
                            line = line.replace(str(foundvar), typevar + string_c + foundvar)
                        else:
                            line = line.replace(str(foundvar), typevar + " " + foundvar)
                            
            if (program_t == True):
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

def main(program_name, program_t, program_com, program_var, slow, ef):
    # language will be in English.
    language = 'en'
    
    # Eventually, this program will be able to tell the edits to a code
    # and give the user the option of starting the TTS at the specific thing
    # they edited

    if (os.path.isfile('Olm_wf.txt') == True):
        os.remove('Olm_wf.txt')

    maketext(program_name, program_t, program_com, program_var, ef)

    tts_text = open('Olm_wf.txt', 'r').read().replace("\n", " ")
    speech  = gTTS(text = str(tts_text), lang = language, slow = slow)
      
    # saving the converted audio in an mp3
    speech.save("Olm_tts.mp3")

if __name__ == '__main__':
    main()
