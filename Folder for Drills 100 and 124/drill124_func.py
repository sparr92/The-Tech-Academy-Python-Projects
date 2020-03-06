import shutil
import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3


import drill124_main
import drill124_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo



#======================================================================================
def create_db(self):
    conn = sqlite3.connect('files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT, \
            col_timestamp TIMESTAMP \
            );")
        conn.commit()
    conn.close()

def select_src(self):
    dir = filedialog.askdirectory()
    self.varBrowse1 = dir
    self.txtBrowse1.insert(0,self.varBrowse1)

def select_dest(self):
    dir = filedialog.askdirectory()
    self.varBrowse2 = dir
    self.txtBrowse2.insert(0,self.varBrowse2)


def check(self):
    conn = sqlite3.connect('files.db')
    with conn:
        cur = conn.cursor()
        source = self.txtBrowse1.get()
        source_file = os.listdir(source)
        destination = self.txtBrowse2.get()
        for file in source_file:
            if file.endswith(".txt"):
                path = os.path.join(source, file)
                mtime = os.path.getmtime(path)
                shutil.move(path,destination)
                cur.execute("INSERT INTO tbl_files(col_filename,col_timestamp) VALUES (?,?)",  (file, mtime))
                print(file)
        conn.commit()
    conn.close()
    


if __name__ == "__main__":
    pass
