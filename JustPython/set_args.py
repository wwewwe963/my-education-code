# การใช้ args '*' ในการรับตัวแปรใน def ได้หลายๆตัวเป็นรูปแบบ tuple []
def average(*scores):
    print(scores)
    sum_score = sum(scores)
    average_score = sum_score / len(scores)
    return average_score

print(average(75, 50, 65))
