f = open('data', 'wb' )
txt = bytes('ยินดีต้อนรับเข้าสู่ Python \n','utf-8')
txt += bytes('โดย ปิยะชาติ จันทะจร','utf-8')
f.write(txt)
f.close()

print("อ่านข้อมูลจาก binary file \n")
f = open('data','rb')
print(f.read())
f.clsoe()