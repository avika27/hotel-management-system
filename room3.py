from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()

        # Title
        lbl_title = Label(self.root, text="Room Booking Details", font=("Arial", 18, "bold"), bg="black", fg="gold", bd=4, relief="ridge")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Label Frame: Room Details
        room_details_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", font=("Arial", 12, "bold"), padx=2)
        room_details_frame.place(x=5, y=50, width=425, height=490)

        # Customer Contact
        lbl_contact = Label(room_details_frame, text="Customer Contact:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_contact.grid(row=0, column=0, sticky=W)
        self.txt_contact = ttk.Entry(room_details_frame, textvariable=self.var_contact, font=("Arial", 13, "bold"), width=29)
        self.txt_contact.grid(row=0, column=1)

        # Other fields omitted for brevity (similar to your existing implementation)

        # Buttons
        btn_frame = Frame(room_details_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btn_add = Button(btn_frame, text="Add", font=("Arial", 12, "bold"), bg="black", fg="gold", command=self.add_data)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", font=("Arial", 12, "bold"), bg="black", fg="gold", command=self.update_data)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", font=("Arial", 12, "bold"), bg="black", fg="gold", command=self.delete_data)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", font=("Arial", 12, "bold"), bg="black", fg="gold", command=self.reset_data)
        btn_reset.grid(row=0, column=3, padx=1)

        # Table Frame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("Arial", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=850, height=490)

        self.room_table = ttk.Treeview(table_frame, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays"), show="headings")
        self.room_table.pack(fill=BOTH, expand=1)

        # Set Table Headings
        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-In")
        self.room_table.heading("checkout", text="Check-Out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Available")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="Days")

        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="lambo", database="HOTEL")
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO room (contact, checkin, checkout, roomtype, roomavailable, meal, noOfdays) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_contact.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noOfdays.get(),
                    )
                )
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Room booking added successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error adding data: {e}")

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="lambo", database="HOTEL")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM room")
            rows = cursor.fetchall()
            if rows:
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                    self.room_table.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

    def update_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a record to update.")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="lambo", database="HOTEL")
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE room SET checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s WHERE contact=%s",
                    (
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noOfdays.get(),
                        self.var_contact.get(),
                    )
                )
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Room booking updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error updating data: {e}")

    def delete_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter a contact number to delete.")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="lambo", database="HOTEL")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM room WHERE contact=%s", (self.var_contact.get(),))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Room booking deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting data: {e}")

    def reset_data(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
