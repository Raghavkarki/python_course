from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
import pymysql

class management:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x800+0+0')
        self.root.title('Library Database Management System')
        self.root.config(bg='#14dede')

        title=Label(self.root,text="Library Database Management System",bd=10,relief=GROOVE,font=('arial',40,'bold'),bg="yellow",fg="red")
        title.pack(side=TOP)
#======================================================All variable
        self.IDnumber_var=StringVar()
        self.Name_var = StringVar()
        self.Contact_var = StringVar()
        self.Address_var = StringVar()
        self.BOOKID_var = StringVar()
        self.BOOKtit_var = StringVar()
        self.Author_var = StringVar()
        self.DateB_var = StringVar()
        self.DateD_var = StringVar()
        self.lrf_var = StringVar()
        self.Dod_var = StringVar()


        self.search_by = StringVar()
        self.search_text = StringVar()





 #=======manage Frame================
        Manage_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=660)

        m_title=Label(Manage_Frame,text="Library Membership Info:",font=('arial',18,'bold'),bg="crimson")
        m_title.grid(row=0,columnspan=2,pady=10)

        lb_IDnumber= Label(Manage_Frame,font=('arial', 12, 'bold'), text="ID number :", padx=2, pady=2,
                                   bg="crimson")
        lb_IDnumber.grid(row=1, column=0,pady=5,padx=10, sticky=W)
        ent_IDnumber = Entry(Manage_Frame,textvariable=self.IDnumber_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE, width=25)

        ent_IDnumber.grid(row=1, column=1,pady=5,padx=10, sticky=W)
        # =========
        lb_NAME= Label(Manage_Frame, font=('arial', 12, 'bold'), text="Name :", padx=2, pady=2,
                                   bg="crimson")
        lb_NAME.grid(row=2, column=0,pady=5,padx=10, sticky=W)
        ent_NAME = Entry(Manage_Frame,textvariable=self.Name_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE, width=25)

        ent_NAME.grid(row=2, column=1,pady=5,padx=10, sticky=W)
        # ================
        lb_Contact = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Contact Number :", padx=2, pady=2,
                              bg="crimson")
        lb_Contact.grid(row=3, column=0,pady=5,padx=10, sticky=W)
        ent_Contact = Entry(Manage_Frame,textvariable=self.Contact_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE, width=25)

        ent_Contact.grid(row=3, column=1,pady=5,padx=10, sticky=W)
        # ==============
        lbl_Address = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Address :", padx=2, pady=2,
                                  bg="crimson")
        lbl_Address.grid(row=4, column=0,pady=5,padx=10, sticky=W)
        ent_Address = Entry(Manage_Frame,textvariable=self.Address_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE, width=25)

        ent_Address.grid(row=4, column=1,pady=5,padx=10, sticky=W)
        # =========
        lb_BOOKID = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Book ID :", padx=2, pady=2,
                                bg="crimson")
        lb_BOOKID.grid(row=5, column=0,pady=5,padx=10, sticky=W)
        ent_BOOKID = Entry(Manage_Frame,textvariable=self.BOOKID_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE, width=25)

        ent_BOOKID.grid(row=5, column=1,pady=5,padx=10, sticky=W)
        # =============
        lb_BOOKtit = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Book Title :", padx=2, pady=2,
                                 bg="crimson")
        lb_BOOKtit.grid(row=6, column=0,pady=5,padx=10, sticky=W)
        ent_BOOKtit = Entry(Manage_Frame,textvariable=self.BOOKtit_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE,  width=25)

        ent_BOOKtit.grid(row=6, column=1,pady=5,padx=10, sticky=W)
        # =============
        lb_Author = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Author Name :", padx=2, pady=2,
                             bg="crimson")
        lb_Author.grid(row=7, column=0,pady=5,padx=10, sticky=W)
        ent_Author = Entry(Manage_Frame,textvariable=self.Author_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE, width=25)

        ent_Author.grid(row=7, column=1,pady=5,padx=10, sticky=W)
        # =================
        lb_DateB = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Date Borrowed:", padx=2, pady=2,
                           bg="crimson")
        lb_DateB.grid(row=8, column=0,pady=5,padx=10, sticky=W)
        ent_DateB = Entry(Manage_Frame,textvariable=self.DateB_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE, width=25)

        ent_DateB.grid(row=8, column=1,pady=5,padx=10, sticky=W)
        # ==========
        lb_lrf = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Late Return Fine :", padx=2, pady=2,
                                 bg="crimson")
        lb_lrf.grid(row=9, column=0,pady=5,padx=10, sticky=W)
        ent_lrf = Entry(Manage_Frame,textvariable=self.lrf_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE,  width=25)

        ent_lrf.grid(row=9, column=1,pady=5,padx=10, sticky=W)
        # ======================2ND COLUMN==========
        lb_Dod = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Date over Due :", padx=2, pady=2,
                               bg="crimson")
        lb_Dod.grid(row=11, column=0,pady=5,padx=10, sticky=W)
        ent_Dod = Entry(Manage_Frame,textvariable=self.Dod_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE,  width=25)

        ent_Dod.grid(row=11, column=1,pady=5,padx=10, sticky=W)
        # ============
        lb_DateD = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Date Due :", padx=2, pady=2,
                                  bg="crimson")
        lb_DateD.grid(row=10, column=0,pady=5,padx=10, sticky=W)
        ent_DateD = Entry(Manage_Frame,textvariable=self.DateD_var, font=('arial', 12, 'bold'),bd=5,relief=GROOVE,  width=25)

        ent_DateD.grid(row=10, column=1,pady=10,padx=10, sticky=W)
        # =================
        self.lb_SL = Label(Manage_Frame, font=('arial', 12, 'bold'), text="Selling Price :", padx=2, pady=2,
                               bg="crimson")
        self.lb_SL.place(x=10,y=520)
        self.txt_SL = Text(Manage_Frame, font=('arial', 12, 'bold'),bd=5,relief=GROOVE,  width=25)

        self.txt_SL.grid(row=12, column=1,pady=1,padx=10, sticky=W)

#=======Buttton Frame======
        btn_Frame = Frame(Manage_Frame, bd=4, bg="crimson", relief=RIDGE)
        btn_Frame.place( x=10,y=560,width=420,height=68)

        btn_Add=Button(btn_Frame,text='Add Data',width=10,command=self.add_books,font=('arial',10,'bold'))
        btn_Add.grid(row=0,column=0,padx=5)

        btn_Update = Button(btn_Frame,command=self.update_data, text='Update Data', width=10,font=('arial',10,'bold'))
        btn_Update.grid(row=0, column=1, padx=5)

        btn_Clear= Button(btn_Frame, text='Clear Data', width=10,font=('arial',10,'bold'),command=self.clear)
        btn_Clear.grid(row=0, column=2, padx=5)

        btn_Delete = Button(btn_Frame,command=self.delete_data, text='Delete Data', width=10,font=('arial',10,'bold'))
        btn_Delete.grid(row=0, column=3, padx=5)

        btn_Exit = Button(btn_Frame, text='Exit', width=10, font=('arial', 10, 'bold'),command=iExit)
        btn_Exit.place(x=150, y=30)



 # =======Detail Frame================
        Detail_Frame = Frame(self.root, bd=6, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=510, y=100, width=800, height=600)

        lb_Search = Label(Detail_Frame, font=('arial', 12, 'bold'), text="Search By :", padx=2, pady=2,bg="crimson")
        lb_Search.grid(row=0, column=0, pady=10, padx=20)
        ent_Search = Entry(Detail_Frame, textvariable=self.search_text,font=('arial', 12, 'bold'), bd=5, relief=GROOVE, width=15)
        ent_Search.grid(row=0, column=2, pady=10, padx=20)


        btn_Search= Button(Detail_Frame,command=self.search_data, text='Search', width=10)
        btn_Search.grid(row=0, column=3, padx=10,pady=10)
        btn_Showall = Button(Detail_Frame,command=self.fecth_data, text='Show All', width=10)
        btn_Showall.grid(row=0, column=4, padx=10,pady=10)



#======combo box========
        combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10, font=('arial', 12, 'bold'),state='readonly')
        combo_Search['value']=('IDnumber','Name','Contact')
        combo_Search.grid(row=0,column=1,pady=10, padx=20)


#============detail show frame=======
        Show_Frame = Frame(Detail_Frame, bd=8, relief=RIDGE, bg="crimson")
        Show_Frame.place(x=20, y=70, width=760, height=510)

        scroll_x=Scrollbar(Show_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Show_Frame, orient=VERTICAL)

        self.libery_table=ttk.Treeview(Show_Frame,columns=('ID number','Name','Contact Number','Address','Book ID','Book Title','Author Name','Date Borrowed','Date Due','Late Return Fine','Date OverDue','Selling Price'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.libery_table.xview)
        scroll_y.config(command=self.libery_table.yview)
        self.libery_table.heading("ID number",text="ID number")
        self.libery_table.heading("Name", text="Name")
        self.libery_table.heading("Contact Number", text="Contact Number")
        self.libery_table.heading("Address", text="Address")
        self.libery_table.heading("Book ID", text="Book ID")
        self.libery_table.heading("Book Title", text="Book Title")
        self.libery_table.heading("Author Name", text="Author Name")
        self.libery_table.heading("Date Borrowed", text="Date Borrowed")
        self.libery_table.heading("Date Due", text="Date Due")
        self.libery_table.heading("Late Return Fine", text="Late Return Fine")
        self.libery_table.heading("Date OverDue", text="Date OverDue")
        self.libery_table.heading("Selling Price", text="Selling Price")
        self.libery_table['show']='headings'
        self.libery_table.column("ID number", width=100)
        self.libery_table.column("Name",width=100)
        self.libery_table.column("Contact Number", width=100)
        self.libery_table.column("Address", width=100)
        self.libery_table.column("Book ID",width=100)
        self.libery_table.column("Book Title", width=100)
        self.libery_table.column("Author Name", width=100)
        self.libery_table.column("Date Borrowed", width=100)
        self.libery_table.column("Date Due",width=100)
        self.libery_table.column("Late Return Fine", width=100)
        self.libery_table.column("Date OverDue", width=100)
        self.libery_table.column("Selling Price", width=100)
        self.libery_table.pack(fill=BOTH,expand=1)
        self.libery_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fecth_data()

    def add_books(self):
        if self.IDnumber_var.get()=="" or self.Name_var.get()=="" or self.Address_var=="" or self.Author_var=="" or self.BOOKID_var==""  or self.BOOKtit_var =="" or self.Contact_var=="" or self.DateB_var=="" or self.DateD_var=="" or self.lrf_var=="" or self.txt_SL=="" :
            messagebox.showerror("ERROR",'All Field Are Required!!')
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="libbooks")
            cur = con.cursor()
            cur.execute("insert into books  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.IDnumber_var.get(),
                                                                                            self.Name_var.get(),
                                                                                            self.Contact_var.get(),
                                                                                            self.Address_var.get(),
                                                                                            self.BOOKID_var.get(),
                                                                                            self.BOOKtit_var.get(),
                                                                                            self.Author_var.get(),
                                                                                            self.DateB_var.get(),
                                                                                            self.DateD_var.get(),
                                                                                            self.lrf_var.get(),
                                                                                            self.Dod_var.get(),
                                                                                            self.txt_SL.get("1.0", END)
                                                                                            ))
            con.commit()
            self.fecth_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has inserted")


    def fecth_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="libbooks")
        cur = con.cursor()
        cur.execute("select * from books")
        rows=cur.fetchall()
        if len(rows)!=0:

            self.libery_table.delete(*self.libery_table.get_children())
            for row in rows:
                self.libery_table.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.IDnumber_var.set('')
        self.Name_var.set('')
        self.Contact_var.set('')
        self.Address_var.set('')
        self.BOOKID_var.set('')
        self.BOOKtit_var.set('')
        self.Author_var.set('')
        self.DateB_var.set('')
        self.DateD_var.set('')
        self.lrf_var.set('')
        self.Dod_var.set('')
        self.txt_SL.delete("1.0", END)

    def get_cursor(self,ev):
        cursor_row=self.libery_table.focus()
        contents=self.libery_table.item(cursor_row)
        row=contents['values']
        self.IDnumber_var.set(row[0])
        self.Name_var.set(row[1])
        self.Contact_var.set(row[2])
        self.Address_var.set(row[3])
        self.BOOKID_var.set(row[4])
        self.BOOKtit_var.set(row[5])
        self.Author_var.set(row[6])
        self.DateB_var.set(row[7])
        self.DateD_var.set(row[8])
        self.lrf_var.set(row[9])
        self.Dod_var.set(row[10])
        self.txt_SL.delete("1.0", END)
        self.txt_SL.insert(END,row[11])


    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="libbooks")
        cur = con.cursor()
        cur.execute("update  books set name Name=%s,Contact=%s,Address=%s,BOOKID=%s,BOOKtit=%s,Author=%s,DateB=%s,DateD=%s,lrf=%s,Dod=%s,SL=%s where IDnumber=%s", (
                                                                                                                                            self.Name_var.get(),
                                                                                                                                            self.Contact_var.get(),
                                                                                                                                            self.Address_var.get(),
                                                                                                                                            self.BOOKID_var.get(),
                                                                                                                                            self.BOOKtit_var.get(),
                                                                                                                                            self.Author_var.get(),
                                                                                                                                            self.DateB_var.get(),
                                                                                                                                            self.DateD_var.get(),
                                                                                                                                            self.lrf_var.get(),
                                                                                                                                            self.Dod_var.get(),
                                                                                                                                            self.txt_SL.get("1.0", END),
                                                                                                                                            self.IDnumber_var.get()
                                                                                                                                            ))

        con.commit()
        self.fecth_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="libbooks")
        cur = con.cursor()
        cur.execute("delete from books where idnumber=%s",self.IDnumber_var.get())
        con.commit()
        con.close()
        self.fecth_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="libbooks")
        cur = con.cursor()

        cur.execute("select * from books where"+str(self.search_by.get())+"LIKE %'"+str(self.search_text.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:

            self.libery_table.delete(*self.libery_table.get_children())
            for row in rows:
                self.libery_table.insert('', END, values=row)
                con.commit()
        con.close()


#====================================================================================for Exit button
def iExit():
    iExit = tkinter.messagebox.askyesno("Library Database Management System", "Confirm if you wanna exit??")
    if iExit > 0:

        wn.destroy()
        return
wn=Tk()
ob=management(wn)
wn.mainloop()







