from tkinter import *
def login():
    yourname=username.get()
    pswd=password.get()
    if yourname=='' or pswd=='':
        message.set("fill the empty field..!")
    else:
      if yourname=="abcd@gmail.com" and pswd=="abc123":
       message.set("Login success")
      else:
       message.set("Wrong username or password..!")
def Loginform():
    global login_scrn
    login_scrn = Tk()
    login_scrn.title("LOGIN FORM")
    login_scrn.geometry("300x250")
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    Label(login_scrn,width="300", text="Please Fill the Details Below", bg="blue",fg="white").pack()
    Label(login_scrn, text="Username * ").place(x=20,y=40)
    Entry(login_scrn, textvariable=username).place(x=90,y=42)
    Label(login_scrn, text="Password * ").place(x=20,y=80)
    Entry(login_scrn, textvariable=password ,show="*").place(x=90,y=82)
    Label(login_scrn, text="",textvariable=message).place(x=95,y=100)
    Button(login_scrn, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_scrn.mainloop()
Loginform()
