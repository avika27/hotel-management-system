from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import string
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # Load the background image
        try:
            self.bg = ImageTk.PhotoImage(file=r"c:\Users\avika\OneDrive\Desktop\taj logo.jpg")
            lbl_bg = Label(self.root, image=self.bg)
            lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load background image: {e}")

        # Load the left-side image
        try:
            self.bg1 = ImageTk.PhotoImage(file=r"c:\Users\avika\OneDrive\Desktop\side reg.jpg")
            left_lbl = Label(self.root, image=self.bg1)
            left_lbl.place(x=220, y=100, width=320, height=550)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load left image: {e}")

        frame = Frame(self.root, bg="yellow")
        frame.place(x=510, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="white", bg="green")
        register_lbl.place(x=20, y=20)

        # Employee Reference
        emp_ref = Label(frame, text="Employee Reference", font=("arial", 15, "bold"), bg="yellow")
        emp_ref.place(x=50, y=60)

        self.var_emp_ref = StringVar()  # Variable for Employee Reference
        self.var_emp_ref.set(self.generate_emp_ref())  # Set generated reference
        self.enty_emp_ref = ttk.Entry(frame, textvariable=self.var_emp_ref, font=("arial", 15, "bold"), state="readonly")
        self.enty_emp_ref.place(x=250, y=60, width=250)

        # First Name
        fname = Label(frame, text="First Name", font=("arial", 15, "bold"), bg="yellow")
        fname.place(x=50, y=100)

        self.var_fname = StringVar()
        self.enty_fname = ttk.Entry(frame, textvariable=self.var_fname, font=("arial", 15, "bold"))
        self.enty_fname.place(x=50, y=130, width=250)

        # Last Name
        lname = Label(frame, text="Last Name", font=("arial", 15, "bold"), bg="yellow")
        lname.place(x=370, y=100)

        self.var_lname = StringVar()
        self.enty_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("arial", 15, "bold"))
        self.enty_lname.place(x=370, y=130, width=250)

        # Contact
        contact = Label(frame, text="Contact", font=("arial", 15, "bold"), bg="yellow")
        contact.place(x=50, y=170)

        self.var_contact = StringVar()
        self.enty_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("arial", 15, "bold"))
        self.enty_contact.place(x=50, y=200, width=250)

        # Email
        email = Label(frame, text="Email ID", font=("arial", 15, "bold"), bg="yellow")
        email.place(x=370, y=170)

        self.var_email = StringVar()
        self.enty_email = ttk.Entry(frame, textvariable=self.var_email, font=("arial", 15, "bold"))
        self.enty_email.place(x=370, y=200, width=250)

        # Security Question
        security_Q = Label(frame, text="Select Security Question", font=("arial", 15, "bold"), bg="yellow")
        security_Q.place(x=50, y=240)

        self.var_security_Q = StringVar()
        self.combo_security_Q = ttk.Combobox(
            frame, textvariable=self.var_security_Q, font=("arial", 13, "bold"), state="readonly"
        )
        self.combo_security_Q['values'] = ("Select", "Your Birthplace", "Your Father's Name", "Your Pet's Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        # Security Answer
        security_A = Label(frame, text="Security Answer", font=("arial", 15, "bold"), bg="yellow")
        security_A.place(x=370, y=240)

        self.var_security_A = StringVar()
        self.enty_security_A = ttk.Entry(frame, textvariable=self.var_security_A, font=("arial", 15, "bold"))
        self.enty_security_A.place(x=370, y=270, width=250)

        # Password
        pswrd = Label(frame, text="Password", font=("arial", 15, "bold"), bg="yellow")
        pswrd.place(x=50, y=310)

        self.var_pswrd = StringVar()
        self.enty_pswrd = ttk.Entry(frame, textvariable=self.var_pswrd, font=("arial", 15, "bold"), show="*")
        self.enty_pswrd.place(x=50, y=340, width=250)

        # Confirm Password
        conpswrd = Label(frame, text="Confirm Password", font=("arial", 15, "bold"), bg="yellow")
        conpswrd.place(x=370, y=310)

        self.var_conpswrd = StringVar()
        self.enty_conpswrd = ttk.Entry(frame, textvariable=self.var_conpswrd, font=("arial", 15, "bold"), show="*")
        self.enty_conpswrd.place(x=370, y=340, width=250)

        # Terms and Conditions
        self.var_checkvar = IntVar()
        checkbtn = Checkbutton(frame, text="I agree to the Terms and Conditions", font=("arial", 12, "bold"),
                               variable=self.var_checkvar, onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # Register Button
        b1 = Button(frame, text="Register", command=self.register_data, font=("arial", 12, "bold"), bg="green", fg="white")
        b1.place(x=50, y=440, width=200)

        # Restart Button
        b2 = Button(frame, text="Restart", command=self.restart_form, font=("arial", 12, "bold"), bg="red", fg="white")
        b2.place(x=250, y=440, width=200)

    def generate_emp_ref(self):
        """Generate a random Employee Reference ID."""
        prefix = "EMP"
        random_number = ''.join(random.choices(string.digits, k=4))
        return f"{prefix}{random_number}"

    def register_data(self):
        if (
            self.var_emp_ref.get() == "" or
            self.var_fname.get() == "" or
            self.var_email.get() == "" or
            self.combo_security_Q.get() == "Select"
        ):
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pswrd.get() != self.var_conpswrd.get():
            messagebox.showerror("Error", "Password and confirm password must match")
        elif not self.var_checkvar.get():
            messagebox.showerror("Error", "Please agree to the terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="lambo", database="HOTEL")
                mycursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                mycursor.execute(query, value)
                row = mycursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    insert_query = """
                    INSERT INTO register (emp_ref, first_name, last_name, contact, email, security_question, security_answer, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    mycursor.execute(insert_query, (
                        self.var_emp_ref.get(),
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.combo_security_Q.get(),
                        self.var_security_A.get(),
                        self.var_pswrd.get(),
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registration Successful")
                    self.refresh_page()  # Refresh the page after success
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}")

    def refresh_page(self):
        """Destroy the current window and reopen the Register class."""
        self.root.destroy()
        root = Tk()
        app = Register(root)
        root.mainloop()

    def restart_form(self):
        """Reset all form fields to empty."""
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_security_Q.set("Select")
        self.var_security_A.set("")
        self.var_pswrd.set("")
        self.var_conpswrd.set("")
        self.var_checkvar.set(0)


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
