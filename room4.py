from tkinter import *
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
from tkinter import ttk
#import random
#import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total=StringVar()

        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("Arial", 18, "bold"), bg="black", fg="gold", bd=4, relief="ridge")
        lbl_title.place(x=0, y=0, width=1595, height=50)

        # Load and display the logo image
        img2 = Image.open("Hotel_logo.jpeg")
        img2 = img2.resize((100, 40), Image.LANCZOS) #LANCZOS?
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img.place(x=5, y=50, width=100, height=40)

        # Label frame for customer details
        self.labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOMBOOKING DETAILS",font=("Arial", 12, "bold"),padx=2)
        self.labelframeleft.place(x=5, y=100, width=425, height=400)
        
        #contact details
        lbl_cust_contact=Label(self.labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        self.enty_contact=ttk.Entry(self.labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=29)
        self.enty_contact.grid(row=0,column=1)

        btnFetchData = Button(self.labelframeleft,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8,command=self.enty_contact)
        btnFetchData.place(x=350,y=4)
        
        #checkin dates
        check_in_dates=Label(self.labelframeleft,text="Check-in dates",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_dates.grid(row=1,column=0,sticky=W)

        self.txtcheck_in_dates =ttk.Entry(self.labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        self.txtcheck_in_dates.grid(row=1,column=1)
        
        #checkout dates
        check_out_dates=Label(self.labelframeleft,text="Check-out dates",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_dates.grid(row=2,column=0,sticky=W)

        self.txtcheck_out_dates =ttk.Entry(self.labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        self.txtcheck_out_dates.grid(row=2,column=1)
        
        #Room Type
        lbl_Room_type=Label(self.labelframeleft,text="room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Room_type.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",passwords="lambo",database="HOTEL")
        my_cursor=conn.cursor()
        my_cursor.execute("select Roomtype from details")
        ide=my_cursor.fetchall()

        self.ComboRoomType=ttk.Combobox(self.labelframeleft,textvariable=self.var_roomtype,font=("arial",13,"bold"),width=29)
        self.ComboRoomType['values']=ide
        self.ComboRoomType.grid(row=3,column=1)

        #Available Room
        lbl_availableroom=Label(self.labelframeleft,text="Check-out dates",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_availableroom.grid(row=4,column=0,sticky=W)

        '''self.txtroomavailable =ttk.Entry(self.labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        self.txtroomavailable.grid(row=4,column=1)'''
        
        conn=mysql.connector.connect(host="localhost",username="root",passwords="lambo",database="HOTEL")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
        self.ComboRoomType=ttk.Combobox(self.labelframeleft,textvariable=self.var_available,font=("arial",13,"bold"),width=29)
        self.ComboRoomType['values']=rows
        self.ComboRoomType.grid(row=4,column=1)


        #meal
        lbl_meal=Label(self.labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_meal.grid(row=5,column=0,sticky=W)

        self.txtmeal =ttk.Entry(self.labelframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        self.txtmeal.grid(row=5,column=1)

        #no. of days

        lbl_days=Label(self.labelframeleft,text="No. of days",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_days.grid(row=6,column=0,sticky=W)

        self.txtdays =ttk.Entry(self.labelframeleft,textvariable=self.var_noOfdays,font=("arial",13,"bold"),width=29)
        self.txtdays.grid(row=6,column=1)

        #paid tax

        lbl_days=Label(self.labelframeleft,text="Paid tax",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_days.grid(row=7,column=0,sticky=W)

        self.txtdays =ttk.Entry(self.labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        self.txtdays.grid(row=7,column=1)

        #Sub Total

        lbl_days=Label(self.labelframeleft,textvariable=self.var_subtotal,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_days.grid(row=8,column=0,sticky=W)

        self.txtdays=ttk.Entry(self.labelframeleft,font=("arial",13,"bold"),width=29)
        self.txtdays.grid(row=8,column=1)

        #TotalCost

        lblIdnumbers=Label(self.labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdnumbers.grid(row=9,column=0,sticky=W)

        self.txtidnumber =ttk.Entry(self.labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        self.txtidnumber.grid(row=9,column=1)
        
        btnBill=Button(self.labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black", fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        btn_frame=Frame(self.labelframeleft,bd=2,relief=RIDGE,pady=2)
        btn_frame.place(x=0,y=344,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black", fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.upgrade_date,font=("arial",11,"bold"),bg="black", fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete-data,font=("arial",11,"bold"),bg="black", fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black", fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=2,pady=2)

        img3 = Image.open("master-bedroom-1-1.jpg")
        img3 = img3.resize((600, 290), Image.LANCZOS) #LANCZOS?
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lbl_img.place(x=450, y=35, width=1295, height=280)

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", font=("Arial", 19, "bold"), padx=2, pady=6)
        Table_Frame.place(x=435, y=270, width=860, height=250)

        lbl_SearchBy = Label(Table_Frame, text="Search By:", font=("Arial", 15, "bold"), bg="gold", fg="black")
        lbl_SearchBy.grid(row=0, column=0, sticky=W)
        self.search_var = StringVar()

        self.combo_Search = ttk.Combobox(Table_Frame, font=("Arial", 12), state="readonly", width=24)
        self.combo_Search['values'] = ("Contact", "Room")
        self.combo_Search.current(0)
        self.combo_Search.grid(row=0, column=1, padx=10, pady=6)
        self.txt_search = StringVar()

        self.txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, width=24, font=("Arial", 12, "bold"))
        self.txtSearch.grid(row=0, column=2, padx=3, pady=6)

        # Search and Show All buttons
        btn_search = Button(Table_Frame, text="Search",command=self.search_data, font=("Arial", 15, "bold"), bg="gold", fg="black")
        btn_search.grid(row=0, column=3, padx=2)

        btn_ShowAll = Button(Table_Frame, text="Show All",command=self.fetch-data, font=("Arial", 15, "bold"), bg="gold", fg="black")
        btn_ShowAll.grid(row=0, column=4, padx=2)

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=60, width=850, height=500)

        # Scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Treeview configuration
        self.room_table = ttk.Treeview(
            details_table,
            columns=("contact", "Checkin", "Checkout", "Room type", "Roomavailable", "meal", "NoOfDays"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # Column configuration for Treeview
        for col in ("contact", "Checkin", "Checkout", "Room type", "Roomavailable", "meal", "NoOfDays"):
            self.room_table.heading(col, text=col)
            self.room_table.column(col, width=100)

        self.room_table["show"] = "headings"
        self.room_table.pack(fill=BOTH, expand=True)
        self.room_table.bind("<ButtonRlease-1>",self.get_cursor())
        self.fetch_data()

def add_data(self):
        if self.var_contact.get()=="" or self.var_heckin.get()=="":
            messagebox.shoerror("error","all fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into room values contact=%s, checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s"(
                self.contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noOfdays.get(),
            ))
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "room Booked", parent=self.root)
                self.clear_data()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
            finally:
                conn.close()

def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",username="root",passwords="",database="")
    my_cursor=conn.cursor()
    my_cursor.execute("select*from room")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        self.room_table.delete(*self.room_table.get-children())
        for i in rows:
            self.room_table.insert("",END,values=i)
            conn.commit()
    conn.close()

def get_cursor(self, event):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']
        self.var_contact.set(row[0]),
        self.var_checkout.set(row[1]),
        self.var_checkin.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOfdays.set(row[6]),

def update_data(self):
        # Update existing customer data
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE room SET Contact=%s, checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s WHERE contact=%s", (
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noOfdays.get(),
                self.var_contact.get(),
            ))
            conn.commit()
            messagebox.showinfo("Success", "Room details have been updated", parent=self.root)
            self.clear_data()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

def delete_data(self):
        if self.var_Ref.get() == "":
            messagebox.showerror("Error", "Select a room record to delete", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM room WHERE ref=%s", (self.var_contact.get(),))
            conn.commit()
            messagebox.showinfo("Success", "Customer has been deleted", parent=self.root)
            self.clear_data()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

def reset(self):
    self.var_contact.set(""),
    self.var_checkout.set(""),
    self.var_checkin.set(""),
    self.var_roomtype.set(""),
    self.var_roomavailable.set(""),
    self.var_meal.set(""),
    self.var_noOfdays.set(""),
    self.var_paidtax.set(""),
    self.var_subtotal.set(""),
    self.var_total.set(""),




'''def fetch_data(self):
        # Display a message box for demonstration
        messagebox.showinfo("Fetch Data", "Data fetched successfully!")
        # Sample data filling for demonstration purposes
        self.enty_contact.insert(0, "1234567890")
        self.txtcheck_in_dates.insert(0, "2024-11-11")
        self.txtcheck_out_dates.insert(0, "2024-11-18")
        self.ComboRoomType.set("Luxury")
        self.txtroomavailable.insert(0, "101")
        self.txtmeal.insert(0, "Breakfast")
        self.txtdays.insert(0, "7")
        self.txtpaidtax.insert(0, "$50")
        self.txtsubtotal.insert(0, "$700")
        self.txttotal.insert(0, "$750")'''      

def enty_contact(self):
    if self.var_contact.get()=="":
        messagebox.showerror()("Error","Please enter contact number",parent=self.root)
    else:
            conn=mysql.connector.connect(host="localhost",username="root",passwords="lambo",database="HOTEL")
            my_cursot=conn.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","this nuber is not found",parent=self.root)
            else:
                conn.commuit()
                conn.close()
                
            showdataframe=frame(self.root,bd=4,relief=RIDGE,padx=2)
            showdataframe.place(x=455,y=55,width=300,height=180)
              
            lblname=label(showDataframe,text="Name:",font=("Arial", 12, "bold"))
            lblname.place(x=0,y=0)
            
            lbl=label(showDataframe,text=row,font=("Arial", 12, "bold"))
            lbl.place(x=90,y=0)

            conn=mysql.connector.connect(host="localhost",username="root",passwords="lambo",database="HOTEL")
            my_cursot=conn.cursor()
            query=("select Gender from customer where mobile=%s")
            value=(self.var_contact.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblGender=label(showDataframe,text="Gender:",font=("Arial", 12, "bold"))
            lblGender.place(x=0,y=30)
            
            lbl2=label(showDataframe,text=row,font=("Arial", 12, "bold"))
            lbl2.place(x=90,y=30)
            
            conn=mysql.connector.connect(host="localhost",username="root",passwords="lambo",database="HOTEL")
            my_cursot=conn.cursor()
            query=("select email from customer where mobile=%s")
            value=(self.var_contact.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblemail=label(showDataframe,text="email:",font=("Arial", 12, "bold"))
            lblemail.place(x=0,y=60)
            
            lbl3=label(showDataframe,text=row,font=("Arial", 12, "bold"))
            lbl3.place(x=90,y=60)

            conn=mysql.connector.connect(host="localhost",username="root",passwords="lambo",database="HOTEL")
            my_cursot=conn.cursor()
            query=("select nationality from customer where mobile=%s")
            value=(self.var_contact.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblnationality=label(showDataframe,text="Nationality:",font=("Arial", 12, "bold"))
            lblnationality.place(x=0,y=60)
            
            lbl4=label(showDataframe,text=row,font=("Arial", 12, "bold"))
            lbl4.place(x=90,y=60)


def search_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            query = "SELECT * FROM room WHERE " + self.combo_Search.get() + " LIKE %s"
            value = "%" + self.txt_search.get() + "%"
            my_cursor.execute(query, (value,))
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.romm_table.delete(*self.romm_table.get_children())
                for row in rows:
                    self.romm_table.insert("", END, values=row)
                conn.commit()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()
            
def total(self):
    indate=self.var_checkin.get()
    outdate=self.var_checkout.get()
    indate=datetime.strptime(indate,"%d%m%Y")
    ondate=datetime.strptime(outdate,"%d%m%Y")
    self.var(noOfdays.set(abs(outdate-indate).days))

    if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="luxary"):
        a1=float(300)
        a2=float(700)
        a3=float(self.var_noOfdays.get())
        a4=float(a1+a2)
        a5=float(a3+a4)
        Tax="Rs."+str("%.2f"%(a5)*0.1)
        ST="Rs."+str("%.2f"%((a5)))
        TT="Rs."+str("%.2f"%(a5)+((a5)*0.1))
        self.var_paidtax.set(Tax)
        self.var_subtotal.set(ST)
        self.var_total.set(TT)

    elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
        a1=float(300)
        a2=float(700)
        a3=float(self.var_noOfdays.get())
        a4=float(a1+a2)
        a5=float(a3+a4)
        Tax="Rs."+str("%.2f"%(a5)*0.1)
        ST="Rs."+str("%.2f"%((a5)))
        TT="Rs."+str("%.2f"%(a5)+((a5)*0.1))
        self.var_paidtax.set(Tax)
        self.var_subtotal.set(ST)
        self.var_total.set(TT)
        
                     

                 
if __name__ == "__main__":
    root=Tk()
    obj= Roombooking(root)
    root.mainloop()