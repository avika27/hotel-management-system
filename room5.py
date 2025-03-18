from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("Arial", 18, "bold"), bg="black", fg="gold", bd=4, relief="ridge")
        lbl_title.place(x=0, y=0, width=1595, height=50)

        # Load and display the logo image
        img2 = Image.open(r"c:\Users\avika\OneDrive\Desktop\taj logo.jpg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img.place(x=5, y=50, width=100, height=40)

        # Label frame for room booking details
        self.labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOMBOOKING DETAILS", font=("Arial", 12, "bold"), padx=2)
        self.labelframeleft.place(x=5, y=100, width=425, height=400)
        
        # Customer contact
        lbl_cust_contact = Label(self.labelframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        self.enty_contact = ttk.Entry(self.labelframeleft, textvariable=self.var_contact, font=("arial", 13, "bold"), width=29)
        self.enty_contact.grid(row=0, column=1)

        btnFetchData = Button(self.labelframeleft, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=8, command=self.enty_contact)
        btnFetchData.place(x=350, y=4)
        
        # Check-in dates
        check_in_dates = Label(self.labelframeleft, text="Check-in dates", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_dates.grid(row=1, column=0, sticky=W)

        self.txtcheck_in_dates = ttk.Entry(self.labelframeleft, textvariable=self.var_checkin, font=("arial", 13, "bold"), width=29)
        self.txtcheck_in_dates.grid(row=1, column=1)
        
        # Check-out dates
        check_out_dates = Label(self.labelframeleft, text="Check-out dates", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_dates.grid(row=2, column=0, sticky=W)

        self.txtcheck_out_dates = ttk.Entry(self.labelframeleft, textvariable=self.var_checkout, font=("arial", 13, "bold"), width=29)
        self.txtcheck_out_dates.grid(row=2, column=1)
        
        # Room Type
        lbl_Room_type = Label(self.labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_Room_type.grid(row=3, column=0, sticky=W)

        self.ComboRoomType = ttk.Combobox(self.labelframeleft, textvariable=self.var_roomtype, font=("arial", 13, "bold"), width=29)
        self.ComboRoomType['values'] = ('Single', 'Double', 'Luxury')
        self.ComboRoomType.grid(row=3, column=1)

        # Available Room
        lbl_availableroom = Label(self.labelframeleft, text="Room Available", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_availableroom.grid(row=4, column=0, sticky=W)

        self.txtroomavailable = ttk.Entry(self.labelframeleft, textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        self.txtroomavailable.grid(row=4, column=1)

        # Meal
        lbl_meal = Label(self.labelframeleft, text="Meal", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)

        self.txtmeal = ttk.Entry(self.labelframeleft, textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        self.txtmeal.grid(row=5, column=1)

        # No. of days
        lbl_days = Label(self.labelframeleft, text="No. of days", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_days.grid(row=6, column=0, sticky=W)

        self.txtdays = ttk.Entry(self.labelframeleft, textvariable=self.var_noOfdays, font=("arial", 13, "bold"), width=29)
        self.txtdays.grid(row=6, column=1)

        # Paid tax
        lbl_days = Label(self.labelframeleft, text="Paid tax", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_days.grid(row=7, column=0, sticky=W)

        self.txtdays = ttk.Entry(self.labelframeleft, textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        self.txtdays.grid(row=7, column=1)

        # Sub Total
        lbl_days = Label(self.labelframeleft, text="Sub Total", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_days.grid(row=8, column=0, sticky=W)

        self.txtdays = ttk.Entry(self.labelframeleft, textvariable=self.var_subtotal, font=("arial", 13, "bold"), width=29)
        self.txtdays.grid(row=8, column=1)

        # Total Cost
        lblIdnumbers = Label(self.labelframeleft, text="Total Cost", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdnumbers.grid(row=9, column=0, sticky=W)

        self.txtidnumber = ttk.Entry(self.labelframeleft, textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
        self.txtidnumber.grid(row=9, column=1)

        # Buttons frame
        btn_frame = Frame(self.labelframeleft, bd=2, relief=RIDGE, pady=2)
        btn_frame.place(x=0, y=344, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.add_data)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.update_data)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.delete_data)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.reset)
        btnReset.grid(row=0, column=3, padx=2, pady=2)

        # Image
        img3 = Image.open(r"c:\Users\avika\OneDrive\Desktop\master-bedroom-1-1.jpg")
        img3 = img3.resize((600, 290), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lbl_img.place(x=450, y=35, width=800, height=290)

        # Treeview for displaying data
        self.RoomBookingTable = ttk.Treeview(self.root, columns=("contact", "checkin", "checkout", "roomtype", "available", "meal", "days", "tax", "subtotal", "total"),
                                              show="headings", height=14)
        self.RoomBookingTable.place(x=450, y=330, width=800, height=190)

        # Define column headings
        self.RoomBookingTable.heading("contact", text="Contact")
        self.RoomBookingTable.heading("checkin", text="Check-in Date")
        self.RoomBookingTable.heading("checkout", text="Check-out Date")
        self.RoomBookingTable.heading("roomtype", text="Room Type")
        self.RoomBookingTable.heading("available", text="Room Available")
        self.RoomBookingTable.heading("meal", text="Meal")
        self.RoomBookingTable.heading("days", text="No. of Days")
        self.RoomBookingTable.heading("tax", text="Paid Tax")
        self.RoomBookingTable.heading("subtotal", text="Sub Total")
        self.RoomBookingTable.heading("total", text="Total Cost")

        self.RoomBookingTable.column("contact", width=100)
        self.RoomBookingTable.column("checkin", width=100)
        self.RoomBookingTable.column("checkout", width=100)
        self.RoomBookingTable.column("roomtype", width=100)
        self.RoomBookingTable.column("available", width=100)
        self.RoomBookingTable.column("meal", width=100)
        self.RoomBookingTable.column("days", width=100)
        self.RoomBookingTable.column("tax", width=100)
        self.RoomBookingTable.column("subtotal", width=100)
        self.RoomBookingTable.column("total", width=100)

        self.RoomBookingTable.pack()

    def add_data(self):
        # Add data functionality (including database logic)
        pass

    def update_data(self):
        # Update data functionality (including database logic)
        pass

    def reset(self):
        # Reset the form fields
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    def delete_data(self):
        # Delete data functionality (including database logic)
        pass

    def fetch_customer_data(self):
        # Fetch customer data based on contact number
        pass


if __name__ == "__main__":
    root = Tk()
    app = Roombooking(root)
    root.mainloop()
