# วิธีการใช้ def lambda อย่างเหมาะสมและถูกต้อง
questions = [
    '    555     ',
    '   2 + 3 = ?   ',
    'what do you want ?     ',
    '   why you leave me ?'
]

zip_questions = [
    '5 x 5 = ?',
    '2 + 3 = ?'
]

zip_answers = [
    '25',
    '5'
]

# - MAP
# --- Map version
cleaned_questions = list(map(lambda q: q.strip().capitalize(), questions))
print(cleaned_questions)
# --- list one-lined version
cleaned_questions = [q.strip().capitalize() for q in questions]
print(cleaned_questions)

# - FILTER
# --- Filter version
filtered_questions = list(filter(lambda q: len(q) >= 6, cleaned_questions))
print(filtered_questions)

# --- list one-lined version
filtered_questions = [q for q in cleaned_questions if len(q) >= 6]
print(filtered_questions)

# - ZIP
# --- Zip version
q_and_a = list(zip(zip_questions, zip_answers))
print(q_and_a)