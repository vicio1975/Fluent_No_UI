# Fluent_No_UI
This app allows one to run Ansys Fluent without using the UI and so to reduce memory usage of your pc/workstation/laptop.
You can select the Fluent version, the jornal file, number of cores and type of analyis (for instance 2D/3D).
The jounal file has to address to the cas (+ dat file if you need) by using the full path.
An example of jounral file is attached to this repository.

The app is released as source code and it also has an executable file.
Best regards,
Vincenzo Sammartano



Note1) how to create exe file from Python script
The Exe file has been created by using "pyinstaller":
1)pip install pyinstaller

2)Go in to the windows shell, then "cd" followed by the location where your Python script is stored
	C:\Users\sammav > cd C:\Users\sammav\Desktop\Test.
	
3)pyinstaller --onefile pythonScriptName.py --icon iconfile.png


Note2)
icon is from <a href="https://www.flaticon.com/free-icons/pizza" title="pizza icons">Pizza icons created by Freepik - Flaticon</a>
