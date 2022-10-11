# import ใช้ในการสร้าง หน้าต่างโปรแกรม
import tkinter as tk

def set_message():
    text = text_input.get()  # เป็นการนำข้อความที่รับมาเก็บไว้
    title_label.configure(text=text)  # เป็นคำสั่งนำตัวแปรที่รับมา แทนที่ในช่องแสดงข้อมูล

window = tk.Tk()
window.title('Calculate')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='เมื่อรักฉันเกิด')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='Okay', command=set_message)
ok_button.pack()

window.mainloop()
