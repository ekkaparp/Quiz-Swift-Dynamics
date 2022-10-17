
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""



number     = int(input())
rom_number = {"1000": "M","500":"D","100": "C","50":"L","10": "X","5":"V","1": "I"}
count      = 1
res        = ""
if number >= 0 and number <= 1000:
    while number > 0 :
        num = number // (10000 // (10 ** count))
        while num > 0 :
            if num % 5 == 4 :
                res += rom_number[str(10000 // (10 ** count))]
                num += 1
                continue
            elif num % 5 == 0 :
                res += rom_number[str(num * 10000 // (10 ** count))]
                num %= 5
            elif num > 5 :
                res += rom_number[str(5 * 10000 // (10 ** count))]
                num -= 5
            else :
                res += rom_number[str(10000 // (10 ** count))] * (num % 5);
                num -= num
        number %= 10000 // (10 ** count)
        count += 1
        
print(res)