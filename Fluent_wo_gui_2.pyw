# -*- coding: utf-8 -*-
"""
Created by Vincenzo Sammartano
email:  v.sammartano@gmail.com
Open points:
done 1.modify the fluent dir ... select with the dir button
2.add the full path of the jou file and meshing option on it
"""
###Libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import os
import subprocess

##Global Vars
#add a file where to read config for ansys
location = os.getcwd()

##Tkinter Window
root = tk.Tk()
root.geometry("250x300+300+300")
root.title("Fluent w/o GUI")
root.resizable(width=False, height=False)
#root.iconbitmap('ansys.ico')

##Fonts
f_H12B = font.Font(family='Helvetica', size=12, weight='bold')
f_H12 = font.Font(family='Helvetica', size=12, weight='normal')
f_H11 = font.Font(family='Helvetica', size=11, weight='bold')
f_H10 = font.Font(family='Helvetica', size=10, weight='bold')
f_H08 = font.Font(family='Helvetica', size=8, weight='normal')
font.families()

####Frames texts
text0 = "Journal file"

# main Frames
top_frame = tk.Frame(root, width=50)
top_frame.grid(row=0, column=0, rowspan=2, sticky="w")

######subframes
frame00 = tk.LabelFrame(top_frame, text=text0, width=100, height=20, font=f_H12B)
frame00.grid(row=1, column=0, padx=5, pady=8, ipadx=5, ipady=5)
frame00.config(borderwidth=2)

frame01 = tk.LabelFrame(top_frame, width=220, height=100, font=f_H12B)
frame01.grid(row=2, column=0, padx=5, pady=8, ipadx=5, ipady=5)
frame01.config(borderwidth=2)

frame11 = tk.LabelFrame(top_frame, width=105, height=100)
frame11.grid(row=3, column=0, padx=12, pady=8, ipadx=1, ipady=5)
frame11.config(borderwidth=2)

frame22 = tk.LabelFrame(top_frame, width=205, height=28)
frame22.grid(row=0, column=0, padx=12, pady=5, ipadx=10, ipady=10)
frame22.grid_propagate(False)
frame22.config(borderwidth=2)

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

def jou():
    """
    This read the journal file
    """
    JF = FS.get() + ".jou"
    #looking for the journal file name
    try:
        if os.path.isfile(JF):
            run_journal(JF)
        else:
            jou_check = tk.Label(frame22, text=JF, font=f_H12B, fg='#f00')
            jou_check.grid(row=0, column=0, padx=5, sticky="E")
            tk.messagebox.showwarning(title="Fluent no GUI", message="This  journal is not here!")
            tk.messagebox.showwarning(title="Fluent no GUI", message="Please select the right journal file.")
    except Exception as e: raise e

def run_journal(file):
    """
    This prepare the command line for fluent
    """
    #### reading the job settings
    # 3d or 2d job
    ddp=''
    if sd.get()==1:
        ddp=' 3ddp'
    elif sd.get()==2:
        ddp=' 2ddp'
    ncores =str(sd_.get())

    ## composing the command line
    ###############################
    fluent_main = fluent_dir()
    ###############################

    fluent_jou = fluent_main + ddp + ' -g -t' + ncores +' -i '
    jou_dir = os.path.join(location,file)
    ##command string 
    com = fluent_jou + jou_dir #+ ' & > monitor.out'
    print(com)
    ###checking the journal file name before lanunching Fluent
    q = tk.messagebox.askyesno(title="Fluent no GUI", message="Is the journal file correct?")
    if q:
        #OS command injection
        command = "cmd /k " + com
        print(command)
        #subprocess.call(command, shell=True)
        os.system(command)
    elif not q:
        tk.messagebox.showwarning(title="Fluent no GUI", message="Please select the right journal file.")

def ACTF():
    """
    This works on radio buttons
    """
    if sd.get()==1:
       sd_1.configure(fg='black')
       sd_2.configure(fg='gray')
    if sd.get()==2:
        sd_1.configure(fg='gray')
        sd_2.configure(fg='black')

###end of Functions
###########################################

###########Main
###Fluent Version
options_list = ["v2021R2", "v2020R1", "ver19"]
value_inside = tk.StringVar(frame22)
# Set the default value of the variable
value_inside.set("v2021R2")
question_menu = tk.OptionMenu(frame22, value_inside, *options_list)
question_menu.grid(row=0, column=1, pady=5)
question_menu.config(font=f_H10, width=10)

f_ver = tk.Label(frame22, text="Fluent ver = ", font=f_H12)
f_ver.grid(row=0, column=0, padx=5, sticky="E")

# INPUT
fs_lab = tk.Label(frame00, text="Journal = ", font=f_H12)
fs_lab.grid(row=0, column=0, padx=5, sticky="E")
FS_ = tk.StringVar()
FS = tk.Entry(frame00, textvariable=FS_, width=15, justify="center", font=f_H12)
FS.grid(row=0, column=1, pady=5)
FS.insert('end', "")
FS.configure(state='normal')

#number of cores
sd_lab = tk.Label(frame01, text="cores = ", font=f_H12)
sd_lab.grid(row=0, column=0, padx=5, sticky="E")
sd_ = tk.StringVar()
sd = tk.Entry(frame01, textvariable=sd_, width=5, justify="center", font=f_H12)
sd.grid(row=0, column=1, pady=5)
sd.insert('end', "1")
sd.configure(state='normal')

#2d or 3d button
sd = tk.IntVar()

sd_1 = tk.Radiobutton(frame01, text = "3ddp", variable = sd,
                 value = 1, height=1, width = 5, font=f_H12)
sd_1.grid(row=1, column=2, pady=1,sticky='W')
sd_1.configure(command=ACTF, indicatoron=1)
sd_1.select()

sd_2 = tk.Radiobutton(frame01, text = "2ddp", variable = sd,
                 value = 2, height=1, width = 5, font=f_H12)

sd_2.grid(row=0, column=2, pady=1,sticky='W')
sd_2.configure(fg='gray')
sd_2.configure(command=ACTF)

##############Buttons
cc = tk.Button(frame11, text="RUN", command=jou, font=f_H12)
cc.config(height=1, width=10)
cc.pack(side='left', fill='x', ipadx=2, padx=3, pady=5)
ex = tk.Button(frame11, text="EXIT", command=ex, font=f_H12)
ex.config(height=1, width=10)
ex.pack(side='right', fill='x', ipadx=2, padx=3, pady=5)
######################

root.mainloop()
