from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Login profile")
root.iconbitmap("amazonIcon.ico")

root.geometry('350x450+0+0')
root.configure(background='#f0f0f0')


def login():
    email = email_entry.get()
    passd = password_entry.get()
    if email == 'pratiktulo42@gmail.com' and passd == "12345678":
        messagebox.showinfo("Greetings", "Successfully Login")
    else:
        messagebox.showwarning("Warning", "Invalid Email or Password")


img = Image.open('AmazonLogo2.png')
resize_img = img.resize((120,90))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image = img)
img_label.pack(pady=10,padx=20)

content_frame = Frame(root, borderwidth=1, relief="solid", padx=10, pady=10)
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

# text label
text_label = Label(content_frame,text="Login",font=('Arial', 18),fg='black')
text_label.pack(anchor='w', pady=(0,20))

email_label = Label(content_frame,text="Email",font=('Arial', 18),fg='black')
email_label.pack(anchor='w', pady=(0,4))

email_entry = Entry(content_frame,font=('Arial', 18),fg='black',bg='#DADADA')
email_entry.pack(fill='x', pady=(0,18))

password_label = Label(content_frame,text="Password",font=('Arial', 18),fg='black')
password_label.pack(anchor='w', pady=(0,4))

password_entry = Entry(content_frame,font=('Arial', 18),fg='black',bg='#DADADA')
password_entry.pack(fill='x', pady=(0,25))

login_btn = Button(content_frame,text="Login",font=('Arial', 18),bg='#F1CF6B',fg='black',bd=2,command=login)
login_btn.pack(fill='x', pady=(0,10))




root.mainloop()