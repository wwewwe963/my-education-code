# การดึง libary tkinter มาใช้
import tkinter as tk

# funciton การคำนวณ สูตรคูณ
def calculate():
    number = 0

    try:
        number = int(number_input.get()) # ทุกครั้งที่ดึงค่ามาใช้ ค่าที่นำมาใช้จะถูก defult เป็น string มาก่อน
        if number == 0:
            raise Exception()
    except:
        output_label.configure(text='false')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + ' * ' + str(i)
        output += ' = ' + str(number*i) + '\n'

    output_label.configure(text=output)

# การกำหนดขนาดต่างๆ และประการศตัวแปร ปุ่ม ช่องกรอกข้อความ ของ หน้าต่างโปรแกรม
window = tk.Tk()
window.title('Calculate')
window.minsize(width=400, height=500)

title_label = tk.Label(master=window, text='การคำนวณสูตรคูณ')
title_label.pack(padx=20, pady=20)

number_input = tk.Entry(master=window, width=30)
number_input.pack(pady=10)

output_button = tk.Button(
    master=window, text='Submit',
    width=20, height=2, command=calculate
)
output_button.pack(pady=10)

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()