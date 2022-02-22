def login():
    username = tb1.get()
    password = tb2.get()
    if username == "admin" and password == "123" :
        messagebox.showinfo("ผลลัพธิ์","ถูกต้อง!")
    else :
       messagebox.showerror("ผลลัพธิ์","ไม่ถูกต้อง!")

from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดยปิยะชาคิ จันทะจร")

lb1 = Label(window,text = "Username :",font = ("Cooper Black",20))
lb1.place(x=50, y=10)
tb1 =Entry(window)
tb1.place(x=250, y=10 , width=200 , height=30)


lb = Label(window,text = "Password:",font = ("Cooper Black",20))
lb.place(x=50, y=50)
tb2 =Entry(window)
tb2.place(x=250, y=50 , width=200 , height=30)

btn = Button(window,text="เข้าสู่ระบบ",font = ("Cooper Black", 17) , command= login)
btn.place(x=260, y=100)

#messagebox.showinfo("","")
#messagebox.showerror("ไม่ถูกตอง","ระวัง")

#main.mainloop()