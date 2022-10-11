# การเขียน และใช้งาน file
file = open('text.txt', 'w')

file.write('ไก่จ๋า ')
file.write('ได้ยินไหมว่าเสียงใคร ')
file.write('อิอิ\n\n')

file.close()

file_read = open('group_scores.txt')
file_write = open('test.txt', 'w')

for group_score in file_read:
    sum_score = 0
    group_score_list = group_score.split(' ')
    for score in group_score_list:
        score_int = int(score)
        sum_score += score_int

    average_score = sum_score / len(group_score_list)
    file_write.write(str(average_score) + '\n')

file_read.close()
file_write.close()
