from tkinter import *
from tkinter import filedialog, messagebox
from playsound import playsound
from shutil import copyfile
import sys
import Olm_main

program_path = ""
def select_path(event):
    global output_path
    output_path = filedialog.askopenfilename()
    globals()['program_path'] = (output_path[output_path.rfind('/')+1:])
    if(make_new_file == False):
        copyfile(program_path,'temp_file.txt')
        globals()[make_new_file] = 1
    path_entry.delete(0, END)
    path_entry.insert(0, output_path)

def btn_clicked():
    Olm_main.main(program_path, (counter_flag % 2), (comments_flag % 2), (variables_flag % 2), (slow_flag % 2), (start_flag % 2))

def trans_clicked():
    playsound('./transcribe_text.mp3')

def make_x(image, name):
    name_needed = ((name[0:name.find('_')]) + "_flag")
    image_needed = ((name[0:name.find('_')]) + "_image_flag")
    if (globals()[image_needed] % 2) == 0:
        image['image'] = img2
        globals()[name_needed] += 1
        globals()[image_needed] += 1
    else:
        image['image'] = img
        globals()[name_needed] = 0
        globals()[image_needed] = 0

window = Tk()
window.title("Olm")
window.geometry("870x700")
window.configure(bg = "#b98b97")


canvas = Canvas(
    window,
    bg = "#ebebeb",
    height = 700,
    width = 870,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle(435, 0, 435 + 435, 0 + 700, fill = "#b98b97", outline="")

title = Label(text="Welcome to Olm!",
              bg = "#ebebeb", fg = "#b98b97",
              font=("Georgia", int(37.0)))
title.place(x = 27.0, y = 25.0)

info_text = Label(text="Olm is an application used to transcribe\n"
                   "Python programs into text-to-speech.\n"
                   "On the right side of this window,\n"
                   "there are five buttons and a select field.\n",
                  bg = "#ebebeb", fg = "#b98b97",
                  justify = "left",
                  font = ("Georgia", int(16.5)))

info_text.place(x = 27.0, y = 100.0)

instructions_text = Label(text="The first button will ask if you want the text\n"
                          "to be slower.\n\n"
                          "The second button is a line counter option.\n\n"
                          "The third button is an ignore comments option.\n\n"
                          "The fourth button will transcribe variable properties\n"
                          "(such as the type of variable, or array size).\n\n"
                          "The fifth button will only transcribe the field you\n"
                          "edited (and everything below).\n\n"
                          "Enter your program path into the select field,\n"
                          "then generate the TTS at the very bottom.",
                  bg = "#ebebeb", fg = "#b98b97",
                  justify = "left",
                  font = ("Georgia", int(12.5)))

instructions_text.place(x = 27.0, y = 230.0)

note_text = Label(text="Please note that larger files will take\n"
                  "longer to process. Do not close Olm when\n"
                  "editing your file.",
                  bg = "#ebebeb", fg = "#b98b97",
                  justify = "left",
                  font = ("Georgia", int(15.5)))

note_text.place(x = 27.0, y = 530.0)

trans_btn_img = PhotoImage(file="./images/trans_img.png")
trans_btn = Button(image = trans_btn_img,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = trans_clicked,
                      relief = "flat")
trans_btn.place(x = 30, y = 610, width = 380, height = 70)



slow_flag = 0
counter_flag = 0
comments_flag = 0
variables_flag = 0
start_flag = 0

img = PhotoImage(file="./images/button_not.png")
img2 = PhotoImage(file="./images/button_true.png")
image_flag = 0
slow_image_flag = 0
counter_image_flag = 0
comments_image_flag = 0
variables_image_flag = 0
start_image_flag = 0

slower_text = Label(text = "Slower text?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(37.0)))
slower_text.place(x = 550.0, y = 30.0)
slow_not_btn_img = img
slow_not_btn = Button(image = slow_not_btn_img,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = make_x,
                      relief = "flat")
slow_not_btn.place(x = 440, y = 5, width = 110, height = 90)
slow_not_btn['command'] = lambda arg = slow_not_btn: make_x(arg, "slow_not_btn")

counter_text = Label(text = "Counter?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(37.0)))
counter_text.place(x = 550.0, y = 120.0)
counter_not_btn = Button(image = slow_not_btn_img,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = make_x,
                      relief = "flat")
counter_not_btn.place(x = 440, y = 95, width = 110, height = 90)
counter_not_btn['command'] = lambda arg=counter_not_btn:make_x(arg, "counter_not_btn")



comments_text = Label(text = "Comments?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(37.0)))
comments_text.place(x = 550.0, y = 210.0)
comments_not_btn = Button(image = slow_not_btn_img,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = make_x,
                      relief = "flat")
comments_not_btn.place(x = 440, y = 185, width = 110, height = 90)
comments_not_btn['command'] = lambda arg=comments_not_btn:make_x(arg, "comments_not_btn")

variables_text = Label(text = "Variables?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(37.0)))
variables_text.place(x = 550.0, y = 300.0)
variables_not_btn = Button(image = slow_not_btn_img,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = make_x,
                      relief = "flat")
variables_not_btn.place(x = 440, y = 275, width = 110, height = 90)
variables_not_btn['command'] = lambda arg = variables_not_btn:make_x(arg, "variables_not_btn")

start_text = Label(text = "Start from where you\n"
                   "last left off?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(23.0)))
start_text.place(x = 550.0, y = 390.0)
start_not_btn = Button(image = slow_not_btn_img,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = make_x,
                      relief = "flat")
start_not_btn.place(x = 440, y = 365, width = 110, height = 90)
start_not_btn['command'] = lambda arg = start_not_btn:make_x(arg, "start_not_btn")


select_file = Label(text = "select file",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Arial-BoldMT", int(25.0)))
select_file.place(x = 460.0, y = 480.0)
path_entry = Entry(bd = 0, bg = "#F6F7F9", highlightthickness = 0)
path_entry.place(x = 460.0, y = 520, width = 380.0, height = 35)
path_entry.bind("<1>", select_path)

make_new_file = 0

generate_btn_img = PhotoImage(file="./images/generate.png")
generate_btn = Button(image = generate_btn_img,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = btn_clicked,
                      relief = "flat")
generate_btn.place(x = 460, y = 570, width = 380, height = 70)

window.resizable(False, False)
window.mainloop()
