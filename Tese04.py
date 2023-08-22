#รับค่า คือ หยุดให้ user ป้อนทางแป้นพิมพ์
#variable (ตัวแปร)

#การแปลงข้องมูล (casting/type comversion)-> str(),int(),float()

StuDentID = input("ป้อน student ID: ")
student_name = input("ป้อน student Name: ")
studentBirthYear = input("ป้อน student Birth Year: ")
print("...............................")
print(f"ยินดีต้อนรับ {StuDentID} {student_name} สู่ SAU")
print(f"คุณเกิดปี {studentBirthYear} แปลว่าคุณอายุ {2023 - int(studentBirthYear)} ปี")
print("ใช้ , ...................................")
print("ยินดีต้อนรับ",StuDentID,student_name,"สู่ SAU")
print("คุณเกิดปี",studentBirthYear,"แปลว่าคุณอายุ",2023 - int(studentBirthYear), "ปี")
print("ใช้ + ...................................")
print("ยินดีต้อนรับ "+StuDentID+" "+student_name+" สู่ SAU")
print("คุณเกิดปี "+studentBirthYear+" แปลว่าคุณอายุ "+2023 - int(studentBirthYear)+" ปี")
print("ใช้ เมธอด formet ........................")
print("ยินดีต้อนรับ {} {} สู่ SAU".format(StuDentID,student_name))
print("คุณเกิดปี {} {} ปี".format(studentBirthYear))





