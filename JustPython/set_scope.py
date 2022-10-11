# scope ลำดับการแสดงผลและนำตัวแปรมาใช้งาน
human1 = 'จับฉ่าย'

def welcome_to_my_world():
    # ตัวแปรที่อยู่ภายใน def จะไม่สามารถนำมาใช้งานข้างนอกได้
    animal1 = 'กระต่าย'
    animal2 = 'กระรอก'
    print(human1 + 'เดินไปเจอ' + animal1)
    print(human2 + 'เดินไปเจอ' + animal2)

human2 = 'แกงอ่อม'

welcome_to_my_world()


# scope ที่อยู่นอกเหนือ def
username = input('Username = ')

error_message = ''
if len(username) < 4:
    error_message = 'น้อยไปจ้า'

print(error_message)
