from tkinter import *
from tkinter import messagebox
import database



def fun(top):
    username=StringVar()
    password=StringVar()
    def save(username,password):
        database.create(username,password)
        messagebox.showinfo("saved","YOur file is saved")
        
    top2=Tk()
    top.destroy()
    top2.title("Create")
    top2.geometry("300x400+200+300")
    user=Label(top2,text="Enter your username").grid(row=2,column=1)
    text=Entry(top2,textvariable=username).grid(row=2,column=2)
    passw=Label(top2,text="Enter your password").grid(row=3,column=1)
    text=Entry(top2,textvariable=password).grid(row=3,column=2)    
    username=str(username)
    password=str(password)        
    btn2=Button(top2,text="Back",command=lambda:main()).grid(row=4,column=1)
    btn=Button(top2,text="Save and login",command=lambda:save(username,password)).grid(row=4,column=2)
    
    print(btn)
    
    top2.mainloop()
    
def main():
    top=Tk()
    top.title("Automation")
    top.geometry('200x300+300+200')
    
    btn = Button(top, text = 'Create', bd = '5', 
                              command = lambda:fun(top))
    btn2 = Button(top, text = 'login', bd = '5', 
                              command = lambda:top.destroy)
    btn.grid(row=2,column=2)
    btn2.grid(row=4,column=2)
    #w =top.Button ( top, command='top option selected' ).flash()
    top.mainloop()
main()
