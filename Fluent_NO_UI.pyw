# -*- coding: utf-8 -*-
"""
Created by Vincenzo Sammartano
email:  v.sammartano@gmail.com

"""
###Libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
import os
#import subprocess

##Tkinter Window
root = tk.Tk()
root.geometry("250x450+300+300")
root.title("Fluent w/o GUI")
root.resizable(width=False, height=False)

#Fonts
f_H12B = font.Font(family='Helvetica', size=12, weight='bold')
f_H12 = font.Font(family='Helvetica', size=12, weight='normal')
f_H11 = font.Font(family='Helvetica', size=11, weight='bold')
f_H10 = font.Font(family='Helvetica', size=10, weight='bold')
f_H08 = font.Font(family='Helvetica', size=8, weight='normal')
font.families()

# main Frames
top_frame = tk.Frame(root, width=50)
top_frame.grid(row=0, column=0, rowspan=2, sticky="w")

######subframes
frame00 = tk.LabelFrame(top_frame, width=40, height=25, text="Journal file",font=f_H12B)
frame00.grid(row=1, column=0,pady=10,ipady=8, padx = 5 , ipadx = 20)
frame00.config(borderwidth=2)

frame22 = tk.LabelFrame(top_frame, width=20, height=25, text="Fluent Version",font=f_H12B)
frame22.grid(row=0, column=0,pady=10,ipady=3, ipadx = 11)
frame22.config(borderwidth=2)
 #frame22.grid_propagate(False)

frame01 = tk.LabelFrame(top_frame, width=220, height=100, text="Cores Number",font=f_H12B)
frame01.grid(row=2, column=0, pady=10, ipady=8, ipadx = 11)
frame01.config(borderwidth=2)

frame11 = tk.LabelFrame(top_frame, width=105, height=100)
frame11.grid(row=5, column=0, padx=12, pady=8, ipadx=1, ipady=5)
frame11.config(borderwidth=2)



frame33 = tk.LabelFrame(top_frame, width=105, height=100, text="Solver type",font=f_H12B)
frame33.grid(row=4, column=0, padx=12, pady=8, ipadx=1, ipady=5)
frame33.config(borderwidth=2)

##########################################

##Functions
def fluent_dir():
    """
    This allows to set the fluent ver and assigns it to a var
    options_list = ["v2021R2", "v2020R1", "ver19"]
    """
    val = value_inside.get()
    if val == "v2021R2":
        return r'"C:\Program Files\ANSYS Inc\v212\fluent\ntbin\win64\fluent.exe"'
    elif val == "v2020R1":
        return r'"C:\Program Files\ANSYS Inc\v201\fluent\ntbin\win64\fluent.exe"'
    elif val == "ver19":
        return r'"C:\Program Files\ANSYS Inc\v19\fluent\ntbin\win64\fluent.exe"'

def ex():
    """
    This destroys the UI
    """
    root.destroy()

def ACTF():
    """
    This works on radio buttons
    """
    if ds.get()==1:
       ds_1.configure(fg='black')
       ds_2.configure(fg='gray')
    if ds.get()==2:
        ds_1.configure(fg='gray')
        ds_2.configure(fg='black')

def switchButtonState():
    if (run_butt['state'] == tk.NORMAL):
        run_butt['state'] = tk.DISABLED
    else:
        run_butt['state'] = tk.NORMAL

def open_j():
    global FS
    journal_name = filedialog.askopenfile(initialdir="/", title="Select Journal File",
                                           filetypes=(("jou", "*.jou"), ("txt", "*.txt")))
    if journal_name:
        FS = str(journal_name.name)
        switchButtonState()


def run_journal():
    """
    This prepare the command line for fluent
    """
    #### reading the job settings
    # 3d or 2d job
    ddp=''
    if ds.get()==1:
        ddp=' 3ddp'
    elif ds.get()==2:
        ddp=' 2ddp'
    ncores = str(sd_.get())

    ## composing the command line
    ###############################
    fluent_main = fluent_dir()
    ###############################
    fluent_jou = fluent_main + ddp + ' -g -t' + ncores +' -i '
    jou_dir = FS
    ##command string
    com = fluent_jou + jou_dir
    # OS command injection
    command = "cmd /k " + com
    os.system (command)

###end of Functions

###########Main

# INPUT
######################
###Fluent Version
options_list = ["v2021R2", "v2020R1", "ver19"]
value_inside = tk.StringVar(frame22)
# Set the default value of the variable
value_inside.set("v2021R2")
question_menu = tk.OptionMenu(frame22, value_inside, *options_list)
question_menu.pack(expand=True)
question_menu.config(font=f_H12, width=8)

#number of cores
sd_ = tk.StringVar()
sd = tk.Entry(frame01, textvariable=sd_, width=8, justify="center", font=f_H12)
sd.pack(expand=True)
sd.insert('end', "1")
sd.configure(state='normal')

#2d or 3d button solver
ds = tk.IntVar()
ds_1 = tk.Radiobutton(frame33, text = "3ddp", variable = ds,
                 value = 1, height=1, width = 5, font=f_H12)
ds_1.grid(row=1, column=2, pady=1,sticky='W')
ds_1.configure(command=ACTF, indicatoron=1)
ds_1.select()
ds_2 = tk.Radiobutton(frame33, text = "2ddp", variable = ds,
                 value = 2, height=1, width = 5, font=f_H12)
ds_2.grid(row=0, column=2, pady=1,sticky='W')
ds_2.configure(fg='gray')
ds_2.configure(command=ACTF)

##############Buttons
#Run button
run_butt = tk.Button(frame11, text="RUN", font=f_H12, command=run_journal,
                     state=tk.DISABLED)
run_butt.config(height=1, width=10)
run_butt.pack(side='left', fill='x', ipadx=2, padx=3, pady=5)

#Exit Button
ex = tk.Button(frame11, text="EXIT", command=ex, font=f_H12)
ex.config(height=1, width=10)
ex.pack(side='right', fill='x', ipadx=2, padx=3, pady=5)

#Journal Button
journal_btn = tk.Button(frame00, text="Open Journal",
                        command =open_j, font=f_H12)
journal_btn.pack(expand=True)
#command = switchButtonState

##########################
root.mainloop()


