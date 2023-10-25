student_height = input("Please enter students heights : \n").split()

students_height_sum = 0
student_height_len = 0

for student_height_num in student_height:
    students_height_sum += int(student_height_num)
    student_height_len += 1

student_height_avg = students_height_sum / student_height_len

print(f"Average student height is : {student_height_avg}")