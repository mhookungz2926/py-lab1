def Checkgrade ():
    Score = int(tb1.get())
    midterm= int(tb2.get())
    final=int(tb3.get())
    mentality=int(tb4.get())
    total= Score+ midterm +final +mentality
    answer.set(total)
    
#nswer = StringVar()

from tkinter  import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมเช็คเกรด โดย ปิยะชาติ จันทะจร")
answer = StringVar()

lb1 =Label(main, text="คะแนนเก็บ: ", font = ("Cooper Black", 14))
lb1.place(x=10,y=20)
tb1 = Entry(main)
tb1.place(x=190, y=20, width= 150, height=30)

lb2 =Label(main, text="คะแนนกลางภาค: ", font = ("Cooper Black", 14))
lb2.place(x=10,y=60)
tb2 = Entry(main)
tb2.place(x=190, y=60, width= 150, height=30)



lb3 =Label(main, text="คะแนนปลายภาค: ", font = ("Cooper Black", 14))
lb3.place(x=10,y=100)
tb3 = Entry(main)
tb3.place(x=190, y=100, width= 150, height=30)


lb4 =Label(main, text="คะแนนจิตพิสัย: ", font = ("Cooper Black", 14))
lb4.place(x=10,y=140)
tb4 = Entry(main)
tb4.place(x=190, y=140, width= 150, height=30)


lb5 =Label(main, text="คำตอบ: ", font = ("Cooper Black", 17))
lb5.place(x=10,y=280)
lb6 =Label(main, font = ("Cooper Black", 17),textvariable=answer)
lb6.place(x=200,y=280)

btn = Button(main,text="คำนวณ",font = ("Cooper Black", 20), command =Checkgrade)
btn.place(x=430, y=20)

main.mainloop()