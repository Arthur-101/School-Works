# Variables and list
tot_stud = 5
tot_sub = 5
total_marks = 500
student_marks_list = []

# Outer loop for students
for student in range(1,tot_stud+1):
    print(f"\nEnter marks for Student {student} :>> ")
    
    subject_marks = []
    
    # Inner loop for Subjects
    for subject in range(1,tot_sub+1):
        mark = float(input(f"  Enter marks for Subject {subject}: "))
        
        subject_marks.append(mark)          # Appending all the subjects marks
    
    student_marks_list.append(subject_marks)       # Appending all the Students Marks

print('\n')

# Calculate the total marks for each student
stud_index = 1
for stud_marks in student_marks_list:
    
    obtained_marks = sum(stud_marks)
    print(f"Total Marks of Student {stud_index} is {obtained_marks}")
    
    percentage = obtained_marks * 100 / total_marks
    print(f"Percentage of Student {stud_index} is {percentage}%")
    
    stud_index += 1
