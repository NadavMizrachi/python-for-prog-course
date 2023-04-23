import tkinter

def save_names():
    global first_name
    global last_name
    print(f' first = {first_name.get()}  last = {last_name.get()}. Doing something...')


window = tkinter.Tk()

first_name = tkinter.StringVar()
last_name = tkinter.StringVar()

window.geometry('600x400+400+200')


first_name_lbl = tkinter.Label(text='First Name:')
first_name_lbl.pack()

first_name_text_box = tkinter.Entry(width=50, textvariable=first_name)
first_name_text_box.pack()


last_name_lbl = tkinter.Label(text='Last Name:')
last_name_lbl.pack()

last_name_text_box = tkinter.Entry(width=50,  textvariable=last_name)
last_name_text_box.pack()

btn1 = tkinter.Button(text="Save", command=save_names)
btn1.pack()
# Show the window
window.mainloop()


