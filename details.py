from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Title Label
        lbl_title = Label(self.root, text="Room Booking Details", font=("Arial", 18, "bold"), bg="black", fg="gold", bd=4, relief="ridge")
        lbl_title.place(x=5, y=0, width=1495, height=50)

        # Load and display the logo image
        img2 = Image.open(r"c:\Users\avika\OneDrive\Desktop\taj logo.jpg")
        img2 = img2.resize((100, 40), Image.LANCZOS)  # LANCZOS?
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img.place(x=5, y=50, width=100, height=40)

        # Label frame for room details
        self.labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("Arial", 12, "bold"), padx=2)
        self.labelframeleft.place(x=5, y=100, width=540, height=350)

        lbl_floor = Label(self.labelframeleft, text="Floor", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()
        self.enty_floor = ttk.Entry(self.labelframeleft, textvariable=self.var_floor, font=("arial", 13, "bold"), width=29)
        self.enty_floor.grid(row=0, column=1)

        lbl_roomno = Label(self.labelframeleft, text="Room No", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_roomno.grid(row=1, column=0, sticky=W)

        self.var_roomno = StringVar()
        self.enty_Roomno = ttk.Entry(self.labelframeleft, textvariable=self.var_roomno, font=("arial", 13, "bold"), width=29)
        self.enty_Roomno.grid(row=1, column=1)

        lbl_roomtype = Label(self.labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_roomtype.grid(row=2, column=0, sticky=W)

        self.var_roomtype = StringVar()
        self.room_type_combo = ttk.Combobox(self.labelframeleft, textvariable=self.var_roomtype, font=("arial", 13, "bold"), width=27, state="readonly")
        self.room_type_combo['values'] = ('Single', 'Double', 'Luxury')  # Options for the combo box
        self.room_type_combo.grid(row=2, column=1)
        self.room_type_combo.set('Single')  # Default selection

        btn_frame = Frame(self.labelframeleft, bd=2, relief=RIDGE, pady=2)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.add_data)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.update_data)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.delete_data)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 11, "bold"), bg="black", fg="gold", width=10, command=self.reset_data)
        btnReset.grid(row=0, column=3, padx=2, pady=2)

        # Table Frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("Arial", 19, "bold"), padx=2, pady=6)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Treeview configuration
        self.room_table = ttk.Treeview(
            Table_Frame,
            columns=("Floor", "RoomNo", "RoomType"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # Column configuration for Treeview
        for col in ("Floor", "RoomNo", "RoomType"):
            self.room_table.heading(col, text=col)
            self.room_table.column(col, width=100)

        self.room_table["show"] = "headings"
        self.room_table.pack(fill=BOTH, expand=True)

        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO room_details (Floor, RoomNo, RoomType) VALUES (%s, %s, %s)", (
                    self.var_floor.get(),
                    self.var_roomno.get(),
                    self.var_roomtype.get(),
                ))
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "New room added", parent=self.root)
                self.clear_data()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
            finally:
                conn.close()

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM room_details")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                    self.room_table.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning", f"Error fetching data: {es}", parent=self.root)

    def update_data(self):
        print("Update button clicked")  # Debugging line
        selected_item = self.room_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a room to update", parent=self.root)
            return

        # Ensure the RoomNo is a valid integer
        room_no_str = self.var_roomno.get().strip()  # Strip any extra spaces from the input

        # Check if RoomNo is a valid integer
        if not room_no_str.isdigit():
            messagebox.showerror("Error", "Room No must be a valid integer", parent=self.root)
            return

        room_no = int(room_no_str)  # Convert the cleaned-up string to an integer

        # Get the current room number from the selected row in the table
        current_room_no = self.room_table.item(selected_item)['values'][1]

        # If the user is changing the RoomNo, check if the new RoomNo already exists
        if room_no != current_room_no:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM room_details WHERE RoomNo=%s", (room_no,))
            existing_room = my_cursor.fetchone()
            if existing_room:
                messagebox.showerror("Error", "RoomNo already exists", parent=self.root)
                conn.close()
                return

        # Now proceed to update the room details
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE room_details SET Floor=%s, RoomNo=%s, RoomType=%s WHERE RoomNo=%s", (
                self.var_floor.get(),
                self.var_roomno.get(),
                self.var_roomtype.get(),
                current_room_no
            ))
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Room details updated", parent=self.root)
            self.clear_data()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

    def delete_data(self):
        selected_item = self.room_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a room to delete", parent=self.root)
            return

        room_no = self.room_table.item(selected_item)['values'][1]

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM room_details WHERE RoomNo=%s", (room_no,))
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Room deleted", parent=self.root)
            self.clear_data()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {es}", parent=self.root)
        finally:
            conn.close()

    def reset_data(self):
        self.clear_data()

    def clear_data(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("Single")


# Create the root window and run the application
root = Tk()
obj = DetailsRoom(root)
root.mainloop()
