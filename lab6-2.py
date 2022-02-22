f = open("myfile2.txt","w")
txt1 = "Siam Dhurakit  \n"
txt1 += "ปิยะชาติ จันทะจร"
s = f.write(txt1)
#s = f.write(txt2)
f.close()

print("เขียนลงไฟล์แล้ว")