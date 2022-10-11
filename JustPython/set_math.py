# Math คำสั่งการคำนวณและหลักการคำนวณโดยใช้ python
import math

set_a = math.floor(32.5)  # result is ปัดเศษลง
set_b = math.ceil(32.5)  # result is ปัดเศษขึ้น
print(set_a)
print(set_b)

scores = [28, 19, 56, 45, 58]
min_score = min(scores)  # result is หาค่าตัวเลขต่ำสุด
max_score = max(scores)  # result is หาค่าตัวเลขสูงสุด
print(min_score)
print(max_score)

# สมการหาความยาวด้านของ สามเหลี่ยมมุมฉาก
a = 6
b = 8
c = math.sqrt(a ** 2 + b ** 2)
print(c)
