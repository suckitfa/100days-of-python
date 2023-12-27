student_heights = input("Input a list of student heights: ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 156 178 165 171 187
total = 0

for h in student_heights:
    total += h
avg_height = total / len(student_heights)
print(f"avg heights = {avg_height}")