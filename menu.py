# Import the tkinter module
import tkinter

# Create the default window
root = tkinter.Tk()
root.geometry('200x100')

# Create the list of options
options_list = ["v2021R2", "v2020R1", "ver19"]

# Variable to keep track of the option
# selected in OptionMenu
value_inside = tkinter.StringVar(root)

# Set the default value of the variable
value_inside.set("v2021R2")

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
question_menu.pack()


# Function to print the submitted option-- testing purpose


def print_answers():
    if value_inside.get() == options_list[0]:
        value = r'"C:\Program Files\ANSYS Inc\v212\fluent\ntbin\win64\fluent.exe"'
    elif value_inside.get() == options_list[1]:
        value = r'"C:\Program Files\ANSYS Inc\v201\fluent\ntbin\win64\fluent.exe"'
    elif value_inside.get() == options_list[2]:
        value = r'"C:\Program Files\ANSYS Inc\v19\fluent\ntbin\win64\fluent.exe"'
    print("Selected Option: {}".format(value))
    return None


# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tkinter.Button(root, text='Submit', command=print_answers)
submit_button.pack()

root.mainloop()