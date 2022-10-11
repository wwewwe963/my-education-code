# การใช้คำสั่ง random ข้อมูล
import random

damage = random.randint(50, 60)  # result is เป็นการสุ่มตัวเลขตั้งแต่ ค่าต่ำสุด - ค่าสูงสุด ตามที่ตั้งไว้
print(damage)

percent = random.uniform(0, 100)  # เป็นคำสั่งที่ใช้ในการ random ข้อมูลตัวเองแบบ float
print(percent)

if percent < 22.5:
    damage *= 2
print(damage)

moneys = [0, 20, 100, 1000]
money = random.choice(moneys)  # เป็นคำสั่งที่ใช้ในการ random list
print(money)

random.shuffle(moneys)  # เป็นคำสั่งที่ใช้ในการ random สลับลำดับแถวข้อมูล
print(moneys)