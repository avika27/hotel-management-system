
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector  # Ensure MySQL connector is properly imported
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom


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
        loginbtn = Button(
            frame,
            command=self.login,
            text="Login",
            font=("times new roman", 15, "bold"),
            bd=3,
            relief=RIDGE,
            fg="white",
            bg="red",
            activebackground="red",
        )
        loginbtn.place(x=110, y=300, width=120, height=35)

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
        """Open the Hotel Management System."""
        self.root.destroy()
        root = Tk()
        app = HotelManagementSystem(root)
        root.mainloop()


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # Define target width and height for the header image and logo
        self.img_width = 950  # Width for the main hotel image
        self.img_height = 300  # Height for the main hotel image
        self.logo_width = 300  # Width for the logo
        self.logo_height = 300  # Height for the logo

        # Load and display the main hotel image
        self.load_image(r"c:\Users\avika\OneDrive\Desktop\taj.jpg", self.img_width, self.img_height, 0)

        # Load and display the logo image next to the main image
        self.load_image(r"c:\Users\avika\OneDrive\Desktop\taj logo.jpg", self.logo_width, self.logo_height, 0, offset=self.img_width)

        # Create and position the title label below the images
        self.create_title_label()

    def load_image(self, image_path, width, height, y_position, offset=0):
        try:
            print(f"Attempting to load image: {image_path}")
            img = Image.open(image_path)
            img = img.resize((width, height), Image.LANCZOS)
            photoimg = ImageTk.PhotoImage(img)

            # Create a Label widget for the image
            lblimg = Label(self.root, image=photoimg, bd=4, relief=RIDGE)
            lblimg.place(x=offset, y=y_position, width=width, height=height)

            # Keep a reference to the photo image to prevent garbage collection
            lblimg.image = photoimg

            print(f"Successfully loaded image: {image_path}")  # Log success
        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")  # Log any other exceptions

    def create_title_label(self):
        title_text = "Hotel Management System"
        lbl_title = Label(self.root, text=title_text, font=("Times New Roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)

        title_width = 1550  # Width of the window
        lbl_width = 800     # Width of the label
        x_position = (title_width - lbl_width) // 2

        lbl_title.place(x=x_position, y=self.img_height, width=lbl_width, height=57)

        main_frame = Frame(self.root, bd=10, relief=RIDGE)
        main_frame.place(x=0, y=350, width=1250, height=400)

        lbl_menu = Label(main_frame, text="MENU", font=("Times New Roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        btn_frame = Frame(main_frame, bd=10, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=210)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.Cust_details, width=22, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking, width=22, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, command=self.DetailsRoom, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="FEEDBACK", width=22, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, command=self.logout, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)
        
        
        img3 = Image.open(r"c:\Users\avika\OneDrive\Desktop\view1.jpg")
        img3 = img3.resize((1310, 375), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        lbling = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbling.place(x=225, y=0, width=1310, height=375)
        
        img4 = Image.open(r"c:\Users\avika\OneDrive\Desktop\tajhall.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        lbling = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbling.place(x=0, y=250, width=230, height=110)

    def Cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def DetailsRoom(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def logout(self):
        result = messagebox.askyesno("Logout", "Are you sure you want to log out?")
        if result:
            self.root.destroy()  # Close the hotel management system window
            root = Tk()
            app = LoginWindow(root)  # Reopen the login window
            root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
