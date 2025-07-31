# income = float(input("Enter your income: "))

# if income <= 250000:
#     print("No tax")
# elif income <= 500000:
#     print("Tax rate: 5%")
# elif income <= 1000000:
#     print("Tax rate: 20%")
# else:
#     print("Tax rate: 30%")



# amount = float(input("Enter purchase amount: "))
# if amount >= 1000:
#     print("You get a 10% discount")
# else:
#     print("No discount")



# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")




# student_score = int(input("Enter student score: "))
# if student_score >= 90:
#     print("Grade: A+")
# elif student_score >= 80:
#     print("Grade: A")
# elif student_score >= 70:
#     print("Grade: B")
# elif student_score >= 60:
#     print("Grade: C")
# else:
#     print("Grade: D")






# result = int(input("Enter result score: "))
# if result >= 33:     
#     print("You passed the exam")
# else:
#     print("You failed the exam")    




# student results# Calculate total marks and percentage, then determine grade
print("Enter marks for each subject:")
Hindi = float(input("Enter marks Hindi: "))
English = float(input("Enter marks English: "))
Math = float(input("Enter marks Math: "))
Science = float(input("Enter marks Science: "))
Computers = float(input("Enter marks Computers: "))

total_marks = Hindi + English + Math + Science + Computers
percentage = total_marks / 5


if Hindi < 33 or English < 33 or Math < 33 or Science < 33 or Computers < 33:
    print("Result: Fail")
else:
    print("Result: Pass")
    

    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'E'
    
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")





# department = input("Enter department: ")
# role = input("Enter role: ")

# if department == "IT":
#     if role == "Developer":
#         print("Assigned to Web App Project")
#     elif role == "Tester":
#         print("Assigned to QA Team")
#     else:
#         print("Unknown Role")
# else:
#     print("Not an IT department")