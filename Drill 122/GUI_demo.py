#!/usr/bin/python
# Python Ver:   3.7
#
# Author:       Sarah Parr
#
# Purpose:      Demonstrating skills learned from working with Tkinter GUI module
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(450,180))
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, width = 24, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse1.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, width = 24, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse2.grid(row=1, column=1, padx=(30,0), pady=(10,0))

        self.btnBrowse = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse.grid(row=0, column=0,padx=(20,0), pady=(30,0), sticky=NE)

        self.btnBrowse = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse.grid(row=1, column=0,padx=(20,0), pady=(7,0), sticky=NE)

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCheck.grid(row=2, column=0,padx=(0,0), pady=(7,0), sticky=NE)

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2)
        self.btnClose.grid(row=2, column=1,padx=(0,0), pady=(7,0), sticky=NE)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
