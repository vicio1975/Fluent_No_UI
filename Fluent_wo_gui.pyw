# -*- coding: utf-8 -*-
"""
Created by Vincenzo Sammartano
email:  v.sammartano@gmail.com
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import os

##Tkinter Window
root = tk.Tk()
root.geometry("250x215+300+300")
root.title("Fluent w/o GUI")
root.resizable(width=False, height=False)
#root.iconbitmap('fan.ico')

##Fonts
f_H12B = font.Font(family='Helvetica', size=12, weight='bold')
f_H12 = font.Font(family='Helvetica', size=12, weight='normal')
f_H11 = font.Font(family='Helvetica', size=11, weight='bold')
f_H10 = font.Font(family='Helvetica', size=10, weight='bold')
f_H08 = font.Font(family='Helvetica', size=8, weight='normal')
font.families()

####Frames texts
text0 = "Jounal file"

# main Frames
top_frame = tk.Frame(root, width=50)
top_frame.grid(row=0, column=0, rowspan=2, sticky="w")

# subframes
frame00 = tk.LabelFrame(top_frame, text=text0, width=100, height=20, font=f_H12B)
frame00.grid(row=0, column=0, padx=5, pady=8, ipadx=5, ipady=5)
frame00.config(borderwidth=2)

frame11 = tk.LabelFrame(top_frame, width=105, height=20)
frame11.grid(row=1, column=0, padx=12, pady=8, ipadx=1, ipady=5)
frame11.config(borderwidth=2)

frame22 = tk.LabelFrame(top_frame, width=195, height=28)
frame22.grid(row=2, column=0, padx=12, pady=5, ipadx=10, ipady=10)
frame22.grid_propagate(False)
frame22.config(borderwidth=2)
##########################################

##Functions

def ex():
    root.destroy()

def jou():
    """
    Thi is the main program
    """
    JF = FS.get() + ".jou"
    try:
        if os.path.isfile(JF):
            run_journal(JF)
    except Exception as e:
        raise e
        print("No journal is in here!")

def run_journal(file):
    fluent_open =    r'"C:\Program Files\ANSYS Inc\v212\fluent\ntbin\win64\fluent.exe"'
    fluent_jou =    fluent_open + ' 3ddp -g -t4 -i '
    jou_dir = os.path.join(location,file)
    com = fluent_jou + jou_dir
    jou_check = tk.Label(frame22, text=file, font=f_H12B)
    jou_check.grid(row=0, column=0, padx=5, sticky="E")
    q = tk.messagebox.askyesno(title="Fluent no GUI", message="Is the journal file correct?")
    if q == True:
        #OS command injection
        command = 'cmd /k ' + com
        print(command)
        os.system(command)
    elif q == False:
        print("not working")
        tk.messagebox.showwarning(title="Fluent no GUI", message="Please select the right journal file.")
   
###end of Functions
###########################################

###########Main    
location = os.getcwd()
# INPUT
fs_lab = tk.Label(frame00, text="Journal = ", font=f_H12)
fs_lab.grid(row=0, column=0, padx=5, sticky="E")
FS_ = tk.StringVar()
FS = tk.Entry(frame00, textvariable=FS_, width=15, justify="center", font=f_H12)
FS.grid(row=0, column=1, pady=5)
FS.insert('end', "")
FS.configure(state='normal')

##############Buttons
cc = tk.Button(frame11, text="RUN", command=jou, font=f_H12)
cc.config(height=1, width=10)
cc.pack(side='left', fill='x', ipadx=2, padx=3, pady=5)
ex = tk.Button(frame11, text="EXIT", command=ex, font=f_H12)
ex.config(height=1, width=10)
ex.pack(side='right', fill='x', ipadx=2, padx=3, pady=5)
######################

root.mainloop()
