# คำสั่ง try except ครอบโค้ด
try:
    x = int(input('X = '))
    y = int(input('Y = '))
    if x == 0:
        raise Exception()  # ทำการคืนค่า except ให้เมื่อเกิดการผิดผลาด
    z = x / y
    print(z)
except:
    print('ผิดที่ไว้ใจ')

print('เส้นทางลูกผู้ชาย')