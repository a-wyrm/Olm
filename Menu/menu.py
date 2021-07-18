from tkinter import *
from tkinter import filedialog, messagebox

def select_path(event):
    global output_path
    output_path = filedialog.askdirectory()
    path_entry.delete(0, END)
    path_entry.insert(0, output_path)

def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title("Olm")
window.geometry("870x580")
window.configure(bg = "#b98b97")

canvas = Canvas(
    window,
    bg = "#ebebeb",
    height = 580,
    width = 870,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle(435, 0, 435 + 435, 0 + 580, fill = "#b98b97", outline="")

title = Label(text="Welcome to Olm!",
              bg = "#ebebeb", fg = "#b98b97",
              font=("Georgia", int(37.0)))
title.place(x = 27.0, y = 50.0)

info_text = Label(text="Olm is an application used to transcribe\n"
                   "Python programs into text-to-speech.\n"
                   "On the right side of this window,\n"
                   "there are four buttons and a text field.\n",
                  bg = "#ebebeb", fg = "#b98b97",
                  justify = "left",
                  font = ("Georgia", int(16.5)))

info_text.place(x = 27.0, y = 150.0)

slower_text = Label(text = "Slower text?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(37.0)))
slower_text.place(x = 550.0, y = 30.0)

counter_text = Label(text = "Counter?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(37.0)))
counter_text.place(x = 550.0, y = 120.0)

comments_text = Label(text = "Comments?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(37.0)))
comments_text.place(x = 550.0, y = 210.0)

variables_text = Label(text = "Variables?",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Georgia", int(37.0)))
variables_text.place(x = 550.0, y = 300.0)

select_file = Label(text = "select file",
                    bg = "#b98b97", fg = "#000000",
                    font = ("Arial-BoldMT", int(25.0)))
select_file.place(x = 460.0, y = 380.0)
path_entry = Entry(bd = 0, bg = "#F6F7F9", highlightthickness = 0)
path_entry.place(x = 460.0, y = 420, width = 380.0, height = 35)
path_entry.bind("<1>", select_path)

generate_btn_img = PhotoImage(file="./images/generate.png")
generate_btn = Button(image = generate_btn_img,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = btn_clicked,
                      relief = "flat")
generate_btn.place(x = 460, y = 470, width = 380, height = 70)

window.resizable(False, False)
window.mainloop()
