import os

import shutil

from tkinter import *
import tkinter as tk


import drill124_gui
import drill124_func


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(800,250))
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        drill124_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
