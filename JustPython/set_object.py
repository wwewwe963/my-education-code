#การใช้งาน object จาก class
import tank # ใช้การ import class จาก ไฟล์อื่นมา
import tkinter as tk

# Tk ก็คือ Class, มี Method ให้เรียกใช้เช่นกัน, Python สร้างมาให้
window = tk.Tk()
window.title('แอ๊บแอ้')
window.minsize(width=400, height=400)

# Tank อันนี้คือ Class ที่เราเป็นคนสร้างเอง
first_tank = tank.Tank('กรุ๊มกริ่ม', 3)
first_tank.name = 'ก๊องแก๊ง'
first_tank.ammo += 2
first_tank.add_ammo(2)

print(first_tank.name)
print(first_tank.ammo)

second_tank = tank.Tank('ฟ๊องแฟ๊ง', 6)
second_tank.add_ammo(3)
second_tank.add_ammo(2)

print(second_tank.name)
print(second_tank.ammo)


third_tank = tank.Tank('งิ้งงอง', 3)
third_tank.fire_ammo()
print(third_tank.ammo)


third_tank.fire_ammo()
third_tank.fire_ammo()
print(third_tank.ammo)

third_tank.add_ammo(4)
print(third_tank.ammo)

window.mainloop()