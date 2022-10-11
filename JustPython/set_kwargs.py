# การใช้ kwargs '**' ในการรับตัวแปรใน def ได้ตามที่รับข้อมูลมา เป็นรูปแบบ dictionary {}
def check_passed(**scores):
    print(scores)
    math = scores.get('math')
    physics = scores.get('physics')
    english = scores.get('english')

    if math is not None and math >= 50:
        print('สอบผ่านคณิต')
    if physics is not None and physics >= 50:
        print('สอบผ่านฟิสิกส์')
    if english is not None and english >= 50:
        print('สอบผ่านอังกฤษ')

check_passed(math=80, physics=35, english=70)