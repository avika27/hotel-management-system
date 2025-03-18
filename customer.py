from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1310x700")

        # Variables for entries
        self.var_Ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_Ref.set(str(x))

        self.var_cust_Name = StringVar()
        self.var_Gender = StringVar()
        self.var_Mobile_No = StringVar()
        self.var_Email = StringVar()
        self.var_Id_proof = StringVar()
        self.var_Id_Number = StringVar()
        self.var_Address = StringVar()

        # Title Label
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("Arial", 18, "bold"), bg="black", fg="gold", bd=4, relief="ridge")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Load and display the logo image
        img2 = Image.open(r"c:\Users\avika\OneDrive\Desktop\taj logo.jpg")
        img2 = img2.resize((400, 195), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img.place(x=0, y=45, width=350, height=195)

        # Label frame for customer details
        self.labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="CUSTOMER DETAILS", padx=2, font=("Arial", 14, "bold"))
        self.labelframeleft.place(x=5, y=240, width=350, height=550)

        # Customer details fields with initial values and read-only state for Customer Ref
        fields = [
            ("Customer Ref", self.var_Ref, 0, "readonly"), 
            ("Customer Name", self.var_cust_Name, 1, "normal"), 
            ("Mobile No", self.var_Mobile_No, 2, "normal"), 
            ("Email", self.var_Email, 3, "normal"), 
            ("ID Proof", self.var_Id_proof, 5, "normal"), 
            ("ID Number", self.var_Id_Number, 6, "normal"), 
            ("Gender", self.var_Gender, 7, "normal"), 
            ("Address", self.var_Address, 8, "normal"), 
        ]

        entries = {}
        for text, variable, row, state in fields:
            lbl = Label(self.labelframeleft, text=text, font=("Arial", 12, "bold"), padx=5, pady=8)
            lbl.grid(row=row, column=0, sticky=W)
            if text in ["ID Proof", "Gender"]:
                combo = ttk.Combobox(self.labelframeleft, textvariable=variable, font=("Arial", 12), state="readonly", width=13)
                if text == "ID Proof":
                    combo['values'] = ("Select", "Aadhar Card", "Driving License", "Other")
                elif text == "Gender":
                    combo['values'] = ("Select", "Male", "Female", "Other")
                combo.current(0)
                combo.grid(row=row, column=1, padx=10, pady=6)
                entries[text] = combo
            else:
                entry = ttk.Entry(self.labelframeleft, textvariable=variable, width=15, font=("Arial", 12), state=state)
                entry.grid(row=row, column=1, padx=10, pady=6)
                entries[text] = entry

        # Buttons
        btn_frame = Frame(self.labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=380, height=40)
        buttons = [
            ("Save", "green", self.save_data),
            ("Clear", "blue", self.clear_data),
            ("Delete", "red", self.delete_data),
            ("Update", "black", self.update_data)  # Update button added
        ]
        for text, color, command in buttons:
            btn = Button(btn_frame, text=text, font=("Arial", 12, "bold"), bg=color, fg="white", command=command)
            btn.pack(side=LEFT, padx=5, fill=X, expand=True)

        # View and Search frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", font=("Arial", 19, "bold"), bg="black", fg="white", padx=2, pady=6)
        Table_Frame.place(x=360, y=70, width=860, height=650)

        lbl_SearchBy = Label(Table_Frame, text="Search By:", font=("Arial", 15, "bold"), bg="gold", fg="black")
        lbl_SearchBy.grid(row=0, column=0, sticky=W)
        self.search_var = StringVar()

        self.combo_Search = ttk.Combobox(Table_Frame, font=("Arial", 12), state="readonly", width=24)
        self.combo_Search['values'] = ("Mobile", "Ref")
        self.combo_Search.current(0)
        self.combo_Search.grid(row=0, column=1, padx=10, pady=6)
        self.txt_search = StringVar()

        self.txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, width=24, font=("Arial", 12, "bold"))
        self.txtSearch.grid(row=0, column=2, padx=3, pady=6)

        # Search and Show All buttons
        btn_search = Button(Table_Frame, text="Search", command=self.search_data, font=("Arial", 15, "bold"), bg="gold", fg="black")
        btn_search.grid(row=0, column=3, padx=2)

        btn_ShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("Arial", 15, "bold"), bg="gold", fg="black")
        btn_ShowAll.grid(row=0, column=4, padx=2)

        # Table Frame for details
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=60, width=850, height=500)

        # Scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Treeview configuration
        self.Cust_details_Table = ttk.Treeview(
            details_table,
            columns=("Ref", "Name", "Gender", "Mobile No.", "Email", "Idproof", "Id Number", "Address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        scroll_x.config(command=self.Cust_details_Table.xview)
        scroll_y.config(command=self.Cust_details_Table.yview)

        # Column configuration for Treeview
        for col in ("Ref", "Name", "Gender", "Mobile No.", "Email", "Idproof", "Id Number", "Address"):
            self.Cust_details_Table.heading(col, text=col)
            self.Cust_details_Table.column(col, width=100)

        self.Cust_details_Table["show"] = "headings"
        self.Cust_details_Table.pack(fill=BOTH, expand=True)

        self.Cust_details_Table.bind("<ButtonRelease-1>", self.get_cursor)

        # Fetch initial data
        self.fetch_data()

    def save_data(self):
        if self.var_Mobile_No.get() == "" or self.var_Email.get() == "":
            messagebox.showerror("Error", "Mobile No. and Email are required fields.", parent=self.root)
            return
        
        # Save new customer data
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO customer (ref, Name, Gender, MobileNo, Email, Idproof, IdNumber, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (
                self.var_Ref.get(),
                self.var_cust_Name.get(),
                self.var_Gender.get(),
                self.var_Mobile_No.get(),
                self.var_Email.get(),
                self.var_Id_proof.get(),
                self.var_Id_Number.get(),
                self.var_Address.get()
            ))
            conn.commit()
            messagebox.showinfo("Success", "Customer details have been saved", parent=self.root)
            self.clear_data()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

    def update_data(self):
        # Update existing customer data
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE customer SET Name=%s, Gender=%s, MobileNo=%s, Email=%s, Idproof=%s, IdNumber=%s, Address=%s WHERE ref=%s", (
                self.var_cust_Name.get(),
                self.var_Gender.get(),
                self.var_Mobile_No.get(),
                self.var_Email.get(),
                self.var_Id_proof.get(),
                self.var_Id_Number.get(),
                self.var_Address.get(),
                self.var_Ref.get()
            ))
            conn.commit()
            messagebox.showinfo("Success", "Customer details have been updated", parent=self.root)
            self.clear_data()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

    def clear_data(self):
        x = random.randint(1000, 9999)  # Generate a new random reference number
        self.var_Ref.set(str(x))  # Set the new reference number
        self.var_cust_Name.set("")
        self.var_Gender.set("Select")
        self.var_Mobile_No.set("")
        self.var_Email.set("")
        self.var_Id_proof.set("Select")
        self.var_Id_Number.set("")
        self.var_Address.set("")
        self.fetch_data()  # Refresh the data view

    def delete_data(self):
        if self.var_Ref.get() == "":
            messagebox.showerror("Error", "Select a customer record to delete", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM customer WHERE ref=%s", (self.var_Ref.get(),))
            conn.commit()
            messagebox.showinfo("Success", "Customer has been deleted", parent=self.root)
            self.clear_data()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM customer")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
                for row in rows:
                    self.Cust_details_Table.insert("", END, values=row)
                conn.commit()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

    def search_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            query = "SELECT * FROM customer WHERE " + self.combo_Search.get() + " LIKE %s"
            value = "%" + self.txt_search.get() + "%"
            my_cursor.execute(query, (value,))
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
                for row in rows:
                    self.Cust_details_Table.insert("", END, values=row)
                conn.commit()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

    def get_cursor(self, event):
        cursor_row = self.Cust_details_Table.focus()
        content = self.Cust_details_Table.item(cursor_row)
        row = content['values']
        self.var_Ref.set(row[0])
        self.var_cust_Name.set(row[1])
        self.var_Gender.set(row[2])
        self.var_Mobile_No.set(row[3])
        self.var_Email.set(row[4])
        self.var_Id_proof.set(row[5])
        self.var_Id_Number.set(row[6])
        self.var_Address.set(row[7])

if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
