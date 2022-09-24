from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
from tkinter.filedialog import askopenfile
import os
#import tkinter.filedialog import askdirectory

#from tkinter.ttk import *


#from tkinter.ttk import *

# Create an instance of tkinter frame
root = tk.Tk()
root.title("GUI")

# Set the geometry of tkinter frame
root.geometry("700x350")





#RadioButton for positive or negative
v = tk.IntVar()
tk.Radiobutton(root,
               text="Positive",
               padx = 10,
               variable=v,
               value=1).grid(row=0,column=0)#.pack(anchor=tk.W)
#btn3.place(relx = 0.5,rely = 0.5,#.pack(anchor=tk.W)anchor =CENTER)

btn4=tk.Radiobutton(root,
               text="Negative",
               padx = 10,
               variable=v,
               value=2).grid(row=1,column=0)#.pack(anchor=tk.W)
#btn4.place(relx = 0.0,rely = 1.0,anchor ="sw")

#create function to upload files from ur pc
def open_file():
   file = filedialog.askopenfile(mode='r')
   if file:
       filepath = os.path.abspath(file.name)
       Label(root, text="File is uploaded : " + str(file.name), font=('Aerial 9')).grid(row=2,column=1)
   # content = file.read()
   #    file.close()
   #    print("%d characters in this file" % len(content))


# Create a Button
btn1 = Button(root, text = 'Select File', command = open_file ,height=0, width=20)
btn1.grid(row=2,column=0)

progress = ttk.Progressbar(root, orient=HORIZONTAL,
                       length=200, mode='determinate')
progress.place(relx = 0.5, rely = 0.8, anchor = CENTER)#grid(row=10,column=10)


# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100


progress.place(relx = 0.5, rely = 0.8, anchor = CENTER)#.pack(pady=10)

# This button will initialize
# the progress bar
label2=tk.Button(root, text='RUN', command=bar)#.pack(pady=10)
label2.place(relx = 0.5, rely = 0.9, anchor = CENTER)#grid(row=500,column=2)


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    #global folder_path
    foldername = filedialog.askdirectory()
    if foldername:
        global folder_path
        folderpath = os.path.abspath(foldername)
        Label(root, text="Folder is uploaded : " + str(foldername), font=('Aerial 9')).grid(row=45, column=1)
        #folder_path.set(foldername)
    #print(filename)



folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Select Folder", command=browse_button,height=0, width=20)
button2.grid(row=45, column=0)


def browse_button2():
    # Allow user to select a directory and store it in global var
    # called folder_path
    #global folder_path
    foldername = filedialog.askdirectory()
    if foldername:
        global folder_path
        folderpath = os.path.abspath(foldername)
        Label(root, text="Output path is uploaded : " + str(foldername), font=('Aerial 9')).grid(row=80, column=1)



folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Output Path", command=browse_button,height=0, width=20)
button2.grid(row=80, column=0)













root.mainloop()









