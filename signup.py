from tkinter import*
from tkinter import messagebox
root = Tk()
def signin():
    username = user.get()
    password = code.get()
    if username == 'niko' and password=='1234':
        scr = Toplevel(root)
        scr.title("HEllloo")
        Label(scr,text="hello everyone",font=("calibri",24,'bold')).pack(expand=True)

    else:
        messagebox.showerror('invalid')

# img = PhotoImage(file='backg.jpg')
lab_img =Label(root,width=600,height=600)
# lab_img.place(x=50,y=50)
frame = Frame(root,width=400,height=400,bg='white')
frame.place(x=800,y=100)
label = Label(frame,text='Sign in',bg='white',font=('verdana',23,'bold'))
label.place(x=100,y=0)

#************************************************
def on_enter(event):
    user.delete(0,'end')
def on_leave(event):
    name = user.get()
    if name =='':
        user.insert(0,'Username')
def enters(event):
    code.delete(0,'end')
def leaves(event):
    name = code.get()
    if name =='':
        code.insert(0,'Password')

user = Entry(frame,width=35,border=0,bg='white',font=('calibri',12))
user.place(x=30,y=80);user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=100)

#password

code = Entry(frame,width=36,borderwidth=0,bg='white',fg='black',font=('calibri',12))
code.place(x=30,y=150);code.insert(0,'Password')
code.bind('<FocusIn>',enters)
code.bind('<FocusOut>',leaves)
Frame(frame, width=295, height=2,bg='black').place(x=25, y=170)

#
button = Button(frame,text='Sign In',bg='blue',fg='white',width=35,font=('calibri',12,'bold'),command=signin).place(x=30,y=200)

label2 = Label(frame,text="Do you have an account?",bg='white',border=0,borderwidth=0,font=('calibri',13)).place(x=30,y=270)
button_qu = Button(frame,text='Sign up',bg='white',fg='blue',width=6,borderwidth=0,relief='solid').place(x=212,y=270)


mainloop()
