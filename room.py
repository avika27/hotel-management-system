import mysql.connector
from tkinter import *

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Room Booking")
        
        # Database connection
        self.conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
        self.my_cursor = self.conn.cursor()

        # Room booking form
        self.contact_label = Label(root, text="Contact")
        self.contact_label.grid(row=0, column=0)
        self.contact_entry = Entry(root)
        self.contact_entry.grid(row=0, column=1)

        self.checkin_label = Label(root, text="Check-in Date")
        self.checkin_label.grid(row=1, column=0)
        self.checkin_entry = Entry(root)
        self.checkin_entry.grid(row=1, column=1)

        self.checkout_label = Label(root, text="Check-out Date")
        self.checkout_label.grid(row=2, column=0)
        self.checkout_entry = Entry(root)
        self.checkout_entry.grid(row=2, column=1)

        self.roomtype_label = Label(root, text="Room Type")
        self.roomtype_label.grid(row=3, column=0)
        self.roomtype_entry = Entry(root)
        self.roomtype_entry.grid(row=3, column=1)

        self.roomavailable_label = Label(root, text="Room Availability")
        self.roomavailable_label.grid(row=4, column=0)
        self.roomavailable_entry = Entry(root)
        self.roomavailable_entry.grid(row=4, column=1)

        self.meal_label = Label(root, text="Meal")
        self.meal_label.grid(row=5, column=0)
        self.meal_entry = Entry(root)
        self.meal_entry.grid(row=5, column=1)

        self.nodays_label = Label(root, text="Number of Days")
        self.nodays_label.grid(row=6, column=0)
        self.nodays_entry = Entry(root)
        self.nodays_entry.grid(row=6, column=1)

        self.submit_button = Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=7, column=1)

    def submit(self):
        # Get data from the form
        contact = self.contact_entry.get()
        checkin = self.checkin_entry.get()
        checkout = self.checkout_entry.get()
        roomtype = self.roomtype_entry.get()
        roomavailable = self.roomavailable_entry.get()
        meal = self.meal_entry.get()
        nodays = self.nodays_entry.get()

        # Insert into database
        try:
            query = """
            INSERT INTO room (contact, checkin, checkout, roomtype, roomavailable, meal, noOfdays)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (contact, checkin, checkout, roomtype, roomavailable, meal, nodays)
            self.my_cursor.execute(query, values)
            self.conn.commit()
            print("Room booking submitted successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.clear_fields()

    def clear_fields(self):
        # Clear form fields after submission
        self.contact_entry.delete(0, END)
        self.checkin_entry.delete(0, END)
        self.checkout_entry.delete(0, END)
        self.roomtype_entry.delete(0, END)
        self.roomavailable_entry.delete(0, END)
        self.meal_entry.delete(0, END)
        self.nodays_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = Roombooking(root)
    root.mainloop()


