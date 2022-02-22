def triangle():
 b = int(base.get())
 h = int(high.get())
 a = 1/2*b*h
 messagebox.showinfo("พื้นที่สามเหลี่ยม","คำตอบ %.2f " % a)
 area.set(a)
from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สามเหลี่ยม โดย ปิยะชาติ จันทะจร")
base = StringVar()
high = StringVar()
area = StringVar()

lb1 =Label(main, text="รับค่าฐาน: ", font = ("Cooper Black", 17))
lb1.place(x=10,y=20)
tb1 = Entry(main, textvariable= base)
tb1.place(x=130, y=20, width= 150, height=30)

lb2 =Label(main,text="รับค่าสูง:", font = ("Cooper Black", 17))
lb2.place(x=10, y=60)
tb2 =Entry(main, textvariable= high)
tb2.place(x=130, y=60, width= 150, height=30)

btn = Button(main,text="คำนวณ",font = ("Cooper Black", 17), command= triangle)
btn.place(x=130, y=100)

lb3 =Label(main,text="คำตอบ:", font = ("Cooper Black", 17))
lb3.place(x=20, y=150)
lb4 =Label(main, bg="#556699", fg="#FFFFFF" ,font = ("Cooper Black", 15), textvariable=area)
lb4.place(x=40, y=200)


main.mainloop()
