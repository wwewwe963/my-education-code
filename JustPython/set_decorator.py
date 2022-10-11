# การใช้ decorator function เพื่อใช้งาน function ไว้ภายในอีกที
def capsule(function):
    def new_function():
        print('เกราะหัว เกราะแขน เกราะอก')
        function()
        print('เกราะขา')
    return new_function # decorator function return function ใหม่ กลับมาที่ def megaman

@capsule # function ถูกส่งเข้า decorator function def capsule
def megaman():
    print('Megaman')

@capsule
def zero():
    print('Zero')

megaman()
zero()
# end decorator

# start new decorator
import math

def pretty_number(function):
    def new_function(*args, **kwargs):
        number = function(*args, **kwargs)
        return '{:.2f}'.format(number)

    return new_function

@pretty_number
def circle_area(redius):
    return math.pi * (redius ** 2)

@pretty_number
def ellipse_area(width, height):
    return math.pi / 4 * width * height


print(circle_area(5))
print(ellipse_area(10, 5))
