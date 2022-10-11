# if elif else
score = 58
if score >= 80:
    print('Grade A')
    print('Ha Ha')
elif score >= 70:
    print('Grade B')
else:
    print('Grade F')

# for in range
for i in range(1, 7):
    if i % 3 == 0:
        break
    print(i)

# def function
def get_box_area(width, length, height):
    if width < 0 or length < 0 or height < 0:
        return 0
    box_area = width * length * height
    return box_area
box1 = get_box_area(4, -4, 2)
box2 = get_box_area(width=1, length=1, height=1)
print(box1)


# modules import function
import shape as s

circle = s.get_circle_area(10)
print(circle)

triangle = s.get_triangle_area(10, 6)
print(triangle)