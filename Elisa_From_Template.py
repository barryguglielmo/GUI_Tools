
# coding: utf-8

# This script is an easy tool to use for ELISA plate analysis and looking at various R&D aspects of ELISA protocols.
# 
# 

# In[1]:


from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd
from PIL import ImageTk, Image


# In[24]:


#define all of my functions for the window
def callback():
    print ("called the callback!")

    
def showImg(image_name, x_loc, y_loc, size):
    load = Image.open(image_name)
    render = ImageTk.PhotoImage(load)
    img = Label( image = render)
    img.image = render
    img.place(x = x_loc, y= y_loc)
    
def browse():
    filename = filedialog.askopenfilename()

    
def selected(vars):
    for i in vars:
        print(str(i.get()))
    print('dahh dahh dahh making nachos dha dah dah for my friends')
        
        
def browse_elisa(): 
    filename = filedialog.askopenfilename()
    excel = pd.read_excel(filename)
    xls = pd.ExcelFile(filename) 
    sheets = xls.sheet_names
    vars = []
    j=1
    for i in sheets:
        vars.append("var"+str(j))
        j+=1
    my_row = 3
    select_all = IntVar(value = 1)
    Checkbutton(root, text = "Select All", variable = select_all, command = callback).grid(row=my_row, sticky=W)
    my_row+=1
    my_col = 3
    tryit = []
    for i in range(0, len(sheets)):
        vars[i] = IntVar(value = 1)
        Checkbutton(root, text = str(sheets[i]), variable = vars[i]).grid(row=my_row, column = my_col, sticky=W)
        my_row+= 1
        if my_row > 10:
            my_col += 2
            my_row = 4
        b = Button(root, text="RUN ANALYSIS", command=selected(vars).grid(row = 2, column = 0))



# In[ ]:


#Make my box
root = Tk()
root.title("ELISA") #title duh
root.geometry("800x800") #size of window

#create a menu
menu = Menu(root)
root.config(menu=menu)
root.configure(background='SkyBlue1')# More Colors at "https://wiki.tcl.tk/37701"

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=browse)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)


elisa_menu = Menu(menu)
menu.add_cascade(label="ELISA", menu=elisa_menu)
elisa_menu.add_command(label="Open...", command=browse_elisa)
elisa_menu.add_separator()
elisa_menu.add_command(label="Exit", command=callback)

math = Menu(menu)
menu.add_cascade(label="Math", menu=math)
math.add_command(label="Dilutions", command=callback)
math.add_command(label="Cook Book", command=callback)
math.add_separator()
math.add_command(label="Exit", command=callback)

#Add Photo
showImg("Ha.png", 0, 0, 20)



root.mainloop()

