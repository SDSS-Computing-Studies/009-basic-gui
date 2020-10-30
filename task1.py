#!python3
"""
Create the interface shown in the file task1.png
You will need to add a function called "multiply"
When the "=" button is clicked, multiply will read 
the contents of the first 2 entry boxes. It will
find the product and display the answer in the
3rd entry box
"""

#importing the necessary commands for tkinter 
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.TK()

def reset():
    currentsum=0
    e1.insert(INSERT,str(currentsum))

currentproduct = 0 


window.mainloop()