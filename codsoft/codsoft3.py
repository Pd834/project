from tkinter import*
import random,string
import pyperclip
root =Tk()
root.geometry("300x300")
username = StringVar()
password = StringVar()
passwordlen = IntVar()
passwordlen.set(0)
def generate_username(name):
    user = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z']
    userstr= ""
    username.get(userstr)
def generate_password(password):

    passstr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    passward = ""
    for x in range(passwordlen.get()):
        passward = passward+random.choice(passstr)
        passwordlen.str(passward)

Label(root,text="password generator").pack()

Label(root,text="username ").pack(pady=3)
Entry(root,textvariable = username).pack(pady=3)
Label(root,text="password length").pack(pady=3)
Entry(root,textvariable = passwordlen).pack(pady=3)
Button(root,text="generate password",command = generate_password).pack(pady=5)
root.mainloop
