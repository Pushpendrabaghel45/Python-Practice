
## Loop examples

# for(ini; condi;increment/decrement) {body}
# for i in range(1, 10):
#     for j in range(i):
#         print(i, end=' ')
#     print()


# for i in range(10, 0, -1):
#     for j in range(i):
#         print("*", end=' ')
#     print()


# for i in range(1, 10):
#     for j in range(10, i, -1):
        
#         print("*", end=' ')
#     print()



# li = ["python", "java", "c++", "javascript"]
# for i in li:
#     print(i)


# tup = ("python", "java", "c++", "javascript")
# for i in tup:
#     print(i)



# s = ("python")
# for i in s:
#     print(i)


# li = ["python", "java", "c++", "javascript"]
# for index in range(len(li)):
#     print(li[index])
# else:
#     print("inside else block")



# cnt = 0
# while (cnt < 5):
#     cnt = cnt + 1
#     print("Hello World")

# else:
#     print("Inside else block")



# # loop control statements
# for p in 'pythonprogramming':
#     if p == 'g' or p == 'r':
#         continue  # Skip the rest of the loop for this iteration
#     print(p)
    

# for p in 'pythonprogramming':
#     if p in ('o'):
#         break  # Exit the loop when 'g' or 'r' is encountered
#     print(p)



# for p in 'pythonprogramming':
#     if p in ('g', 'r'):
#         pass  # Do nothing for 'g' or 'r'
#     print(p)  # Print other characters




##function examples

# def fun():
#     print("Hello, World!")
# fun()


# def evenOdd(x: int) -> str:
#     if x % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(evenOdd(7))
# print(evenOdd(16))



# def customfun():
#     print("welcome")

# print("Hello")

# customfun()
# print("test")
# customfun()
# print("sumit")
# customfun()
# print("Frameboxx")
# customfun()



# def addition(x,y):
#     print(x+y)

# addition(10, 20)
# addition(30, 40)
# addition(50, 60)
# addition(70, 80)


# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")
# def greet(name):
#     return(f"Hello, {name}!")

#     print(greet('Alice'))


# def myFun(y, x=50):
#     print("x: ", x)
#     print("y: ", y)


# myFun(10)



# def student(fname, lname):
#     print(fname, lname)

# student(fname='Shyamu', lname='Rana')
# student(lname='Golu', fname='Singh')





# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)

# print("Case-1:")
# nameAge("Suraj", 27)

# # print("\nCase-2:")
# # nameAge("Sumit", 30)




##loop & function examples
# student management system

students = [{"name": "Het patel", "roll": "123", "marks": 402},
            {"name": "Pushpendra Baghel", "roll": "124", "marks": 450},
            {"name": "Kavya Sharma", "roll": "125", "marks": 480},
            {"name": "Shailesh Kumar", "roll": "126", "marks": 470},
            {"name": "Gourav Kapur", "roll": "127", "marks": 490}]  # List to store student records

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    student = {"name": name, "roll": roll, "marks": marks}
    students.append(student)
    print(f"✅ Student {name} added successfully!")

def view_students():
    if not students:
        print("No students found!")
        return
    print("\n=== Student Records ===")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found: Name: {s['name']}, Marks: {s['marks']}")
            return
    print("Student not found!")

def average_marks():
    if not students:
        print("No data to calculate average!")
        return
    total = sum(s["marks"] for s in students)
    avg = total / len(students)
    print(f"Average Marks: {avg:.2f}")

def topper():
    if not students:
        print("No data to find topper!")
        return
    top = max(students, key=lambda x: x["marks"])
    print(f"🏆 Topper: {top['name']} with {top['marks']} marks")

# Main Loop
#while False:
while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll")
    print("4. Calculate Average Marks")
    print("5. Find Topper")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        average_marks()
    elif choice == "5":
        topper()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.")



