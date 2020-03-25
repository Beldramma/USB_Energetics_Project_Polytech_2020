The USB_Energetics_Spy program is designed to display six measurement curves, voltage,
current and energy input and output from .txt files, examples can be found in the "data" folder.
Because there was a network problem when putting the package on Pypi, the pip installation is not available at the moment.
Make sure you have python and pip installed.
To install the package, clone the following repository: https://github.com/Beldramma/USB_Energetics_Project_Polytech_2020 .
After that, go to this folder, where you will find several files and folders including the setup.py file.
In this folder, open a command terminal and type :
Under Windows:
"python -m pip install ."

Under Linux :
"pip install."

This will install the USB_Energetics_Spy package, and the required dependencies, including wxmplot, wxpython and numpy.

After that, run the following command:
"python -m USB_Energetics_Spy"

A window will then appear, with a "Print Plots" button.
Press it and select one of the .txt data files, available here as an example.
Another window will then appear, displaying 6 measurement curves.
