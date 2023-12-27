student_heights = input("Input a list of student heights: ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 156 178 165 171 187
total = sum(student_heights)
num_of_student = len(student_heights)
avg_height = total / num_of_student
print(f"avg heights = {avg_height}")