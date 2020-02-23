
from tkinter import filedialog
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 350))
        self.master.title('Drill 123')
        self.master.config(bg='lightgray')

        self.lblDisplay1 = Label(self.master,text='Please select a file directory: ', font=("Helvetica", 12), fg='black', bg='lightgray')
        self.lblDisplay1.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay2 = Label(self.master,text='', font=("Helvetica", 12), fg='black', bg='lightgray')
        self.lblDisplay2.grid(row=3, column=0,padx=(30,0), pady=(30,0))
        
        self.btnSelect = Button(self.master, text="Select Folder", width=10, height=2, command=self.select)
        self.btnSelect.grid(row=1, column=1,padx=(0,0), pady=(30,0), sticky=NW)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90), pady=(30,0), sticky=NW)

    def select(self):
        dir = filedialog.askdirectory()
        self.lblDisplay2.config(text='{}'.format(dir))

    def cancel(self):
        self.master.destroy()
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
