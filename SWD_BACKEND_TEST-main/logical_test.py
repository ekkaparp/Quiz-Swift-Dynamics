
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

number    = int(input())
thai_text = {"0":"ศูนย์","01":"เอ็ด","1":"หนึ่ง","2":"สอง","3":"สาม","4":"สี่","5":"ห้า","6":"หก","7":"เจ็ด","8":"แปด","9":"เก้า","10":"สิบ","20":"ยี่สิบ","100":"ร้อย","1000":"พัน","10000":"หมื่น","100000":"แสน","1000000":"ล้าน","10000000":"สิบล้าน"}
word      = ""
if number >= 0 and number <= 10000000 :
    num = str(number)
    for index in range(len(num)):
        if len(num) > 1 and index == (len(num) - 1) and  num[index] == "1" :
            if num[index-1] == "0" :
                word += thai_text["1"]
            else :
                word += thai_text["01"]
        elif len(num) - index == 2 and num[index] in ["1","2"]   :
            word += thai_text[str(10 * int(num[index]))]
            continue
        elif len(num) > 1 and num[index] == "0"   :
            continue
        else :
            word += thai_text[num[index]]
        
        if len(num) - index != 1 :
            
            word += thai_text[str(10 ** (len(num) - index - 1))]
print(word)