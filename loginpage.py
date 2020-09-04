from tkinter import*
import tkinter.messagebox
from management import*
import os
import pickle


class login_system:
    def __init__(self,window):
        self.wn = window
        self.wn.geometry('900x500')
        self.wn.title(' Login Page')
        self.wn.config(bg='#14dede')

#=================================frame
        title = Label(self.wn, text="Login Page", bd=10, relief=GROOVE,
                      font=('arial', 40, 'bold'), bg="yellow", fg="red")
        title.pack(side=TOP)

        login_Frame = Frame(self.wn, bd=6, relief=RIDGE, bg="crimson")
        login_Frame.place(x=180, y=100, width=550, height=250)

        self.lb_IDnumber = Label( login_Frame, font=('arial', 20, 'bold'), text="User ID :", padx=2, pady=2,
                                 bg="crimson")
        self.lb_IDnumber.grid(row=1, column=0, pady=5, padx=10 )
        self.ent_IDnumber = Entry( login_Frame, font=('arial', 20, 'bold'), bd=5, relief=GROOVE, width=20)

        self.ent_IDnumber.grid(row=1, column=1, pady=5, padx=10)
        # =========
        self.lb_pass = Label( login_Frame, font=('arial', 20, 'bold'), text="Password :", padx=2, pady=2,
                             bg="crimson")
        self.lb_pass.grid(row=2, column=0, pady=5, padx=10)
        self.ent_pass = Entry( login_Frame, font=('arial', 20, 'bold'), bd=5, relief=GROOVE, width=20, show='*')

        self.ent_pass.grid(row=2, column=1, pady=5, padx=10)

#=====================================================================================btn frame==
        btn_Frame = Frame(login_Frame, bd=4, bg="crimson", relief=RIDGE)
        btn_Frame.place( x=35,y=135,width=480,height=78)

        self.btn_login = Button(btn_Frame, text='Login', width=25, font=('arial', 20, 'bold'),command=self.btn_login_click)
        self.btn_login.place(x=20, y=10)

    def btn_login_click(self):
        if self.ent_IDnumber.get() == '' or self.ent_pass.get() == '':
            tkinter.messagebox.showerror('credential error', 'please fill the form completely')

        elif self.ent_IDnumber.get()=="66891" and self.ent_pass.get()=="12345":
            tkinter.messagebox.showinfo("Successfull",f"Welcome{' Raghav Karki'}")
            management = Tk()
            management(management)


        else:
            tkinter.messagebox.showerror("Error","Invalid ID or Password")




wn=Tk()
ob=login_system(wn)
wn.mainloop()