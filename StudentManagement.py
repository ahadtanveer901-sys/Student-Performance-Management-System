# Mini University Management System

print("=========================================")
print("          STUDENT REPORT")
print("=========================================")

# Student Information
name = input("Enter your name: ")
roll_no = input("Enter your roll number: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
semester = int(input("Enter your semester: "))

print("\n=========================================")
print("        ACADEMIC INFORMATION")
print("=========================================")

# Subject Marks
programming_marks = int(input("Enter your programming marks: "))
database_marks = int(input("Enter your database marks: "))
mathematics_marks = int(input("Enter your mathematics marks: "))
ai_marks = int(input("Enter your AI marks: "))
english_marks = int(input("Enter your English marks: "))

# Academic Calculations
total_marks = (
    programming_marks
    + database_marks
    + mathematics_marks
    + ai_marks
    + english_marks
)

average_marks = total_marks / 5

print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)

print("\n=========================================")
print("        ATTENDANCE INFORMATION")
print("=========================================")

attendance_percentage = float(
    input("Enter attendance percentage: ")
)

attendance_status = (
    "Good" if attendance_percentage >= 75 else "Poor"
)

print("Attendance Percentage:", attendance_percentage)
print("Status:", attendance_status)

print("\n=========================================")
print("           FEE INFORMATION")
print("=========================================")

total_semester_fee = int(input("Enter total semester fee: "))
paid_fee = int(input("Enter paid fee: "))

remaining_fee = total_semester_fee - paid_fee

fee_status = "Paid" if remaining_fee == 0 else "Not Paid"

print("Total Fee:", total_semester_fee)
print("Paid Fee:", paid_fee)
print("Remaining Fee:", remaining_fee)
print("Fee Status:", fee_status)

print("\n=========================================")
print("        END OF STUDENT REPORT")
print("=========================================")