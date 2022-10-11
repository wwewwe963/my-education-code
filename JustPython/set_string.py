# การใช้งาน String
message = 'อมก๋อย'
tel = '0831426548'
text = 'JustPython'
pre_list = 'กระต่าย, กระรอก, หมี'

count = len(message) # ผลลัพล์เป็น นำชุดข้อความแสดงเป็นจำนวน
condition = 'ก๋อย' in message  # ผลลัพล์เป็น True
check_type = tel.isdigit()  # ผลลัพล์เป็น True
upper = text.upper()  # ผลลัพล์เป็น ข้อความตัวใหญ่
replace = text.replace('Python', 'Rabbit')  # ผลลัพล์เป็น ข้อความถูกแทนที่
animals = pre_list.split(', ') # ผลลัพล์เป็น การแยกชุดข้อความออกเป็น list
new_measage = ', '.join(animals) # ผลลัพล์เป็นการรวม list เป็นชุดข้อความ

print(new_measage)
