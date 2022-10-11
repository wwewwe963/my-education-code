# lambda เป็นคำสั่งที่ใช้ในการสร้าง def ออกมาเพืยงแค่บรรทัดเดียวเท่านั้น
def clean_text(text): return text.strip().capitalize()
# capitalize คือคำสั่งที่ทำหน้าที่ในการกำหนด str ตัวแรกของประโยคให้เป็นตัวใหญ่ แล้วข้อความชุดที่เหลือเป็นตัวเล็กทั้งหมด

clean_text_2 = lambda text: text.strip().capitalize()

input_firstname = '     LAMBDA'
output_firstname = clean_text_2(input_firstname)
print(output_firstname)

input_lastname = ' oungoung     '
output_lastname = clean_text_2(input_lastname)
print(output_lastname)