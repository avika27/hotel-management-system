from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from hotel import HotelManagementSystem  # Importing the HotelManagementSystem class

def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Login")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"c:\Users\avika\OneDrive\Desktop\login page background.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Login Logo
        img1 = Image.open(r"c:\Users\avika\OneDrive\Desktop\login.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(frame, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=120, y=10, width=100, height=100)

        # "Get Started" Label
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Employee ID
        firstnamelbl = Label(frame, text="Employee ID", font=("times new roman", 15, "bold"), fg="white", bg="black")
        firstnamelbl.place(x=70, y=150)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password
        passwordlbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        passwordlbl.place(x=70, y=215)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register Button
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"), bd=3, borderwidth=0,
                             fg="white", bg="black", command=self.register_window)
        registerbtn.place(x=15, y=350, width=160)

        # Forgot Password Button
        pswrdbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"), bd=3, borderwidth=0,
                          fg="white", bg="black")
        pswrdbtn.place(x=8, y=370, width=160)

    def login(self):
        """Verify login credentials."""
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "Please enter Employee ID and Password")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="lambo", database="HOTEL"
                )
                my_cursor = conn.cursor()
                emp_ref = self.txtuser.get().strip()
                password = self.txtpass.get().strip()

                # Query to verify credentials
                my_cursor.execute(
                    "SELECT * FROM register WHERE emp_ref=%s AND password=%s",
                    (emp_ref, password),
                )
                row = my_cursor.fetchone()

                if row:
                    messagebox.showinfo("Success", "Login Successful")
                    self.open_hotel_management()  # Open the hotel management system
                else:
                    messagebox.showerror("Error", "Invalid Employee ID or Password")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")
            finally:
                if conn.is_connected():
                    conn.close()

    def open_hotel_management(self):
        """Open the Hotel Management System interface."""
        self.new_window = Toplevel(self.root)
        HotelManagementSystem(self.new_window)  # Launch the Hotel Management System
        self.root.withdraw()  # Hide the login window

    def register_window(self):
        """Open the registration window."""
        self.new_window = Toplevel(self.root)
        Register(self.new_window)
        self.root.withdraw()  # Hide the login window

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        # Similar to previous register window implementation
        # Define registration fields and database insertion logic here.

if __name__ == "__main__":
    main()
