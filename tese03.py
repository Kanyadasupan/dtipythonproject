#แสดงข้อมูลหลายๆประเภทใน print เดียว
#1.  ใฃ้, โดยที่มันจะมี spece ในแต่ละ,
print("SAU",5555,55,666666,True,12+3)
#2. ใช้ + มีข้อแม้ ข้อมูลที่ไม่ใช้ string ต้องแปลเป็น string และไม่มี spece ไม่เหมือนกัน
print("SAU"+str(555)+' '+str(123.456)+' '+str(True)+' '+str(23+67))
#3. ใช้เมธอตดชื่อ format
print("SAU {} {} {} {}".format(555,123,456,True,10+4))
print("SAU {0} {2} {9} {7}".format(555,123,456,True,10+4))
#4. ใช้ f-string ***
print(f"SAU {555} {123.456} {True} {10+4}")
#........................
#กรณี 1 บรรทัดมีหลายเ statmen ให้คั้นด้วย ; (statmen= คำสั่ง)
print("aaa");print(111);Print(False)
