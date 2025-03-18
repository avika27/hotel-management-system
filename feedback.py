from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class HotelManagementSystem:
    # Initialize the window
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")  # Default size
        
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
            img = Image.open(image_path)
            img = img.resize((width, height), Image.LANCZOS)
            photoimg = ImageTk.PhotoImage(img)
            
            # Create a Label widget for the image
            lblimg = Label(self.root, image=photoimg, bd=4, relief=RIDGE)
            lblimg.place(x=offset, y=y_position, width=width, height=height)

            # Keep a reference to the photo image to prevent garbage collection
            lblimg.image = photoimg
        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")  # Log any other exceptions

    def create_title_label(self):
        # Create and position the title label centered below the images
        title_text = "Hotel Management System"
        lbl_title = Label(self.root, text=title_text, font=("Times New Roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        
        # Calculate x position to center the title
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
        
        # Existing buttons
        cust_btn = Button(btn_frame, text="CUSTOMER", width=22, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)
        
        # New Feedback Button
        feedback_btn = Button(btn_frame, text="FEEDBACK", width=22, command=self.open_feedback_window, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        feedback_btn.grid(row=1, column=0, pady=1)
        
        # Other existing buttons
        room_btn = Button(btn_frame, text="ROOM", width=22, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=2, column=0, pady=1)
        
        details_btn = Button(btn_frame, text="DETAILS", width=22, command=self.DetailsRoom, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=3, column=0, pady=1)
        
        report_btn = Button(btn_frame, text="REPORT", width=22, font=("Times New Roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=4, column=0, pady=1)

    def open_feedback_window(self):
        self.new_window = Toplevel(self.root)
        self.app = FeedbackWindow(self.new_window)


class FeedbackWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Feedback")
        self.root.geometry("500x400+0+0")

        # Feedback Form Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=50, y=50, width=400, height=300)

        # Title Label
        lbl_title = Label(frame, text="Write Your Feedback", font=("times new roman", 20, "bold"), fg="white", bg="black")
        lbl_title.place(x=100, y=10)

        # Feedback Textbox
        self.feedback_text = Text(frame, font=("times new roman", 12), width=30, height=8, wrap=WORD)
        self.feedback_text.place(x=40, y=50)

        # Submit Button
        submit_btn = Button(frame, text="Submit Feedback", font=("times new roman", 15, "bold"), bg="green", fg="white", command=self.submit_feedback)
        submit_btn.place(x=150, y=220)

    def submit_feedback(self):
        feedback = self.feedback_text.get("1.0", "end-1c")  # Get feedback text

        if feedback.strip() == "":
            messagebox.showwarning("Input Error", "Please write some feedback before submitting.", parent=self.root)
        else:
            try:
                # Connect to the MySQL database
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
                cursor = conn.cursor()

                # Insert the feedback into a 'feedback' table (you need to create this table in your database)
                cursor.execute("INSERT INTO feedback (feedback_text) VALUES (%s)", (feedback,))
                conn.commit()

                messagebox.showinfo("Feedback", "Thank you for your feedback!", parent=self.root)
                self.root.destroy()  # Close the feedback window

                # Close the cursor and connection
                cursor.close()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error occurred: {e}", parent=self.root)


# Main Program
if __name__ == "__main__":
    root = Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
