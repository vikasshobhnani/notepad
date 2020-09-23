from tkinter import *
from tkinter import messagebox as tsmg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    win.title("untitled - notepad")
    file = None
    textarea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*,txt")])
    if file == "":
        file = None
    else:
        win.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*,txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            win.title(os.path.basename(file) + "- Notepad")
            print("file saved")

    else:
        f = open(file, "w")
        f.write(textarea.get(1.0,END))
        f.close()
def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def quit():
    win.destroy()

def about():
    tsmg.showinfo("notepad", "nodepad- a text editor by vikas shobhnani")

if __name__ == '__main__':
    win = Tk()
    win.geometry("500x500")
    win.title("notepad")
    file = None
    mainmenu = Menu(win)

    m1 = Menu(mainmenu, tearoff=0)
    m1.add_command(label="New", command=newfile)
    m1.add_command(label="Open", command=openfile)
    m1.add_command(label="Save", command=savefile)
    m1.add_separator()
    m1.add_command(label="Exit", command=quit)
    win.configure(menu=mainmenu)
    mainmenu.add_cascade(label="File", menu=m1)

    m2 = Menu(mainmenu, tearoff=0)
    m2.add_command(label="Cut", command=cut)
    m2.add_command(label="Copy", command=copy)
    m2.add_command(label="Paste", command=paste)
    win.configure(menu=mainmenu)
    mainmenu.add_cascade(label="Edit", menu=m2)

    m3 = Menu(mainmenu, tearoff=0)
    m3.add_command(label="About", command=about)
    win.configure(menu=mainmenu)
    mainmenu.add_cascade(label="Help", menu=m3)

    textarea = Text(win, font="lucida 10")
    textarea.pack(expand=True, fill=BOTH)

    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)
    win.mainloop()