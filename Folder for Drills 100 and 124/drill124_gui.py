from tkinter import *

import drill124_main
import drill124_func



def load_gui(self):

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, width=70, font=("Helvetica", 10), fg='black', bg='white')
        self.txtBrowse1.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, width=70, font=("Helvetica", 10), fg='black', bg='white')
        self.txtBrowse2.grid(row=1, column=1, padx=(30,0), pady=(10,0))

        self.btnBrowse1 = Button(self.master,width=20,height=1,text="Select source directory...",command=lambda: drill124_func.select_src(self))
        self.btnBrowse1.grid(row=0, column=0,padx=(20,0), pady=(30,0), sticky=NE)

        self.btnBrowse2 = Button(self.master,width=24,height=1,text="Select destination directory...",command=lambda: drill124_func.select_dest(self))
        self.btnBrowse2.grid(row=1, column=0,padx=(20,0), pady=(7,0), sticky=NE)

        self.btnCheck = Button(self.master,width=15,height=2,text="Check for files...",command=lambda: drill124_func.check(self))
        self.btnCheck.grid(row=2, column=0,padx=(0,0), pady=(7,0), sticky=NE)


        drill124_func.create_db(self)



if __name__ == "__main__":
    pass
