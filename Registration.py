from tkinter import*
root = Tk()
root.geometry('600x600')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=80,y=60)


label_1 = Label(root, text="FullName",width=20,font=("bold", 12))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 12))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 12))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 6, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 18, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Age:",width=20,font=("bold", 12))
label_4.place(x=70,y=280)


entry_2 = Entry(root)
entry_2.place(x=240,y=280)

Button(root, text='Submit',width=20,bg='navy',fg='white').place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("Registration Form  successfully created")
