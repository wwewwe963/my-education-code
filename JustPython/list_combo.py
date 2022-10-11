# list
quests = ['ปลูกต้นมะม่วง', 'ล่วงปลาไหล', 'ไล่ศัตรูพืช']

# การใช้ list กำหนดเงือนไข
if 'ไล่ศัตรูพืช' in quests:
    print('ท่านเข้าเมืองได้')

# การใช้งาน list ตามเงือนไข
max_quest = 5
if len(quests) < max_quest:
    quests.append('จับปลาดุก')
    print(quests)

# การใช้งาน list แบบวน loop
for quest in quests:
    print(quest)

# การใช้งาน list วน loop แบบนำไปใช้แสดงผลข้อความ
for i in range(len(quests)):
    print(str(i + 1) + '. ' + quests[i])

