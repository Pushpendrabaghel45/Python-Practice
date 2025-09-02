                        #   Part A: Introduction & Variables (5 Tasks)

# #1.  Write a Python program to swap two variables without using a third variable.

# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))

# a = a + b
# b = a - b


# print(a)
# print(b)


# #2.  Create a program that takes your name and age as input and prints them in a sentence.

# name = input("Enter your name:")
# age = input("Enter your age:")

# print(f"My name is {name} and I am {age} year old")


# 3. Write a program to calculate the area of a rectangle using user input for length and width.

# length = float(input("Enter the length of rectangle:"))

# width = float(input("Enter the width of rectangle:"))

# area = length * width
# print(f"area of the rectangle is {area} square")


# # 4. Store your favorite movie name, release year, and rating in variables and print them in a formatted string.

# movie_name = "Hanuman"
# release_year = 2025
# rating = 9.2

# print(f"My favorite movie is {movie_name}, and release {release_year},with ratting of {rating}/10.")


# # 5. Write a program to convert temperature from Celsius to Fahrenheit.

# Celsius = 20

# Fahrenheit= (Celsius * 9/5) + 40

# print(Fahrenheit)



                            # Part B: Data Types (int, float, str, boolean) (10 Tasks)

# #   1. Take input from the user and check its data type using type().


# user = 52.20

# print(type(user))


# # 2.Write a program that accepts two integers and prints their sum, difference, product, and quotient.

# a = 50

# b = 80

# print("Sum:", a + b)
# print("Difference:", a - b)

# print("Product:", a * b)
# print("quotient:", a/b)


# #  3. Create a program that checks whether a given number is even or odd.


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# # 4. Write a program that accepts a string and prints its length.

# user = input("Enter a string: ")

# print("Length of string:", len(user))



# # 5. Store a boolean value (True/False) in a variable and use it in a decision (if condition)

# user = False

# if user:
#     print("Condition is right.")
# else:
#     print("Condition is not right.")


# # 6. Write a program to check whether a string is a palindrome or not.

# s = input("Enter a string: ")

# if s == [1]:
#     print("It's a palindrome.")
# else:
#     print("Not a palindrome.")


# # 7. Convert a float number to an integer and print both values.

# num  = float(input("Enter a float number: "))
# int_num = int(num)

# print("Float:", num)
# print("Integer:", int_num)


# # 8.Take a string input and display the first and last character.

# text = input("Enter a string: ")

# if len(text):
#     print("First character:", text[0])
#     print("Last character:", text[-1])
# else:
#     print("no character")


# # 9. Write a program that checks whether the entered number is positive, negative, or zero

# num = float(input("Enter the number: "))

# if num > 1:
#     print("positive:")
# elif num < 1:
#     print("negative:")
# else:
#     print("zero")

# # 10. Concatenate two strings and print the result with proper formatting.

# user1 = input("Enter first string:")
# user2 = input("Enter first string:")

# str = user1 + user2

# print("String concatenate",(str))



                #  Part C: Operators (10 Tasks)


# # 1. Write a program that calculates the square and cube of a given number using exponent operator 

# num = 12

# square = num ** 2
# cube = num ** 3

# print("square:", square)
# print("cube:", cube)


# # 2.Demonstrate the use of // (floor division) and % (modulus) operators.

# a = 36
# b = 6

# print("floor division:", a // b)
# print("modulus:", a % b)


# # 3. Write a program that takes three numbers and prints the largest one using comparison operators


# a = input("Enter first number")
# b = input("Enter second number")
# c = input("Enter three number")

# if a > b and a > c:
#     largest = a
# elif b > a and b > c:
#     largest = b
# else:
#     largest = c

# print("largest number is ", largest)

# # 4. Use logical operators (and, or, not) in a program to check eligibility for voting (age ≥ 18 and citizenship = True).

# age = int(input("Enter your age: "))
# citizenship = input("Are you a citizen? (yes/no): ")

# if age >= 18 and citizenship == "yes":
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# # 5. Write a program to check if a number is divisible by both 3 and 5.

# num = int(input("Enter a number"))

# if num % 3 ==0  and num % 5 == 0:
#     print("divisible by 3 or 5")
# else:
#     print("not divisible by 3 or 5")


# # 6. Show the difference between == and is operators with examples.

# a = [8,5,6]
# b = [8,5,6]
# print(a == b)
# print(a is b)


# # 7. Write a program to calculate simple interest (SI = PRT/100).

# p = 8000
# r = 10
# t = 6

# si = p*r*t /100

# print ("result", si)


# # 8. Demonstrate assignment operators (+=, -=, *=, /=, etc.) on a variable.

# x = 50
# print("value of x", x)

# x += 10
# print(x)

# x -= 15
# print(x)

# x *= 12
# print(x)

# x /= 5
# print(x)

# # 9. Write a program to calculate BMI (Body Mass Index).

# weight = int(input("Enter your weight..kilograms:"))
# height = int(input("Enter your height..meters:"))

# bmi = weight / (height ** 2)


# print("Your BMI is:",bmi)

# # 10. Create a program to find the remainder when one number is divided by another

# num1 = int(input("Enter the num: "))
# num2 = int(input("Enter the num: "))

# remainder = num1 % num2

# print(f"The remainder {num1} divided by {num2} is {remainder}")


            #    Part D: Conditional Statements (15 Tasks)


# # 1. Write a program to check if a given year is a leap year


# year = int(input("Enter a year: "))

# if (year % 4 == 0) and (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# # 2.Take marks of a student and display the grade (A, B, C, D, Fail).


# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else:
#     print("Fail")

# # 3.Write a program to check if a character is a vowel or consonant.

# char = input("Enter character: ")

# if char in "aeiou":
#     print("Vowel")
# else :
#     print("Consonant")


# # 4.Create a login system that asks for username and password. If correct, print "Login successful"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Invalid")

# # 5. Write a program to classify a person’s age group (Child, Teen, Adult, Senior).

# age = int(input("Enter your age: "))

# if age < 13:
#     print("Child")

# elif age < 20:
#     print("Teen")

# elif age < 60:
#     print("Adult")

# else:
#     print("Senior")



# # 6.Check if a number is prime.


# num = int(input("Enter a number"))





# # 7.  Write a program to find the smallest of three numbers.

# a = input("Enter first number")
# b = input("Enter second number")
# c = input("Enter three number")
# print("smallest number is", min(a,b,c))


# # 8.Create a simple calculator using if-elif-else (add, subtract, multiply, divide).
  

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# option = input("Choose option(+, -, *, /): ")

# if option == '+':
#     print( a + b)

# elif option == '-':
#     print( a - b)

# elif option == '*':
#     print( a * b)

# elif option == '/':
#     print( a / b)
  
# else:
#     print("Invalid")


# # 9.Take two numbers and check if the first is a multiple of the second


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(f"{a} is a multiple of {b}")


# # 10.Write a program to check if a number is a perfect square.

# import math
# num = int(input("Enter a number: "))
# sqr = math.isqrt(num)
# if sqr * sqr == num:
#     print("Perfect square")
# else:
#     print("Not a perfect square")


# # 11. Create a discount calculator: if purchase > 1000 give 10% discount else no discount.

# amount = float(input("Enter purchase amount: "))
# if amount > 1000:
#     discount = amount * 10/100
#     print(discount)
#     print("discount price:", amount - discount)
# else:
#     print(f"No discount: {amount}")


# # 12. Write a program to check whether a given character is uppercase, lowercase, digit, or special symbol.

# a = input("Enter a character: ")

# if a.isupper():
#     print("Uppercase")
# elif a.islower():
#     print("Lowercase")
# elif a.isdigit():
#     print("Digit")
# else:
#     print("symbol")


# # 13. Ask the user to enter their exam marks and print "Pass" if ≥ 40 else "Fail".


# marks = int(input("Enter your exam marks: "))

# if marks >= 40:
#     print("Pass")

# else:
#     print("Fail")


# # 14. Write a program to check whether the entered password length is strong (≥8) or weak.


# password = input("Enter password:")

# if len(password) >= 8:
#     print("Strong password")
    
# else:
#     print("Weak password")


# # 15. Write a program that checks whether a number ends with digit 0.


# num = int(input("Enter a number: "))

# if str(num).endswith('0'):
#     print("Ends with 0")
    
# else:
#     print("Does not end with 0")



                # Part E: Loops (10 Tasks)


# # 1.Print all even numbers from 1 to 50.


# e = 50

# for e in range(1,50):
#     if e % 2 == 0:
#         print(e)


# # 2. Print multiplication table of a number entered by the user.

# num = 10

# for i in range(1,10):

#     multiple = num * i
#     print(multiple)


# # 3. Write a program to find the factorial of a number using a loop.

# num = 3
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial is:", factorial)


# # 4. Print Fibonacci sequence up to n terms.

# n = 10
# a, b = 0, 1
# for i in range(n):
#     print(a, end ='')
#     a , b = b, a + b
    


# # 5. Print the sum of digits of a number.

# num = int(input("Enter the number"))

# total = 0

# while num > 0:
    
# print("Sum of digits:", total)   ###Dought hai isme




# 6. Write a program to reverse a number using loops.

# num  = int(input("Enter a number:"))

# rev = 0
# while num > 0:
  
# print("Reversed number:", rev)


# # 7. Write a program to count the number of vowels in a given string.


# num = input("Enter a string:")

# count = 0
# for b in num:
#     if b in 'aeiou':
#         count  += 1
# print("Number of vowles:" ,count)

# # 8. Print a pattern:


# for i in range(1, 10):
#     for j in range(i):
#         print("*", end=' ')
#     print()




# 9. Write a program to check whether a number is an Armstrong number.


##dought hai




# # 10. Write a program to print all prime numbers between 1 and 100.


# for num in range(1, 100):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num)


