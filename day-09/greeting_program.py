def grade(score):
    grade = ''
    if score >= 91 and score <= 100:
        grade = 'Outstanding'
    elif score >= 81 and score <= 90:
        grade = 'Exceed Expecations'
    elif score >= 71 and score <= 80:
        grade = 'Acceptable'
    elif score <= 70:
        grade = 'Fail'
    return grade

student_scores = {
    "Harry":81,
    "Ron":78,
    "Herminoe":99,
    "Draco":74,
    "Neville":62
}

student_grades = {}

for k in student_scores:
    student_grades[k] = grade(student_scores[k])

print(student_grades)