def cal():
    r = int(tb1.get())
    circle = (3.14)*r*r
    messagebox.showinfo("พื้นที่วงกลม","ผลลัพธ์ %.2f" % circle)
    result.set(circle)

from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดย ปิยะชาติ จันทะจร")

result = StringVar()

lb = Label(window , text="ยินดีต้อนรับเข้าสู่ python",font=("Tahoma",24))
lb.place(x=50, y=10)

lb2 = Label(window , text="รับค่ารัศมี",font=("Tahoma",18))
lb2.place(x=50,y=80)

lb3 = Label(window , text="แสดงผลลัพธ์",font=("Tahoma",18))
lb3.place(x=50,y=140)


tb1 = Entry(window)
tb1.place(x=210, y=90)

tb2 = Entry(window , textvariable = result)
tb2.place(x=210, y=150)

btn = Button(window, text="คำนวณ", font=("Tahoma",18), command=cal)
btn.place(x=400, y=100 )
   
window.mainloop()
             
             
             
             
             
             
             
             
             
             
             
             