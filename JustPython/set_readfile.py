# การอ่าน และใช้งาน file
file = open('scores.txt')

pass_count = 0
for score in file:
    score_int = int(score)
    if score_int >= 50:
        pass_count += 1

print('Student passed = ' + str(pass_count))

file.close()

file1 = open('group_scores.txt')

group_count = 0
for group_scores in file1:
    group_scores_list = group_scores.split(' ')
    for score_in in group_scores_list:
        score_num = int(score_in)
        if score_num >= 50:
            group_count += 1

print('Student Passed = ' + str(group_count))

file1.close()