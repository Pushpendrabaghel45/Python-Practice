# 1.  Create a program that takes your name and age as input and prints them in a sentence.

# name = input("Enter your name:")
# age = input("Enter your age:")

# print(f"My name is {name} and I am {age} year old")


# 2. Store your favorite movie name, release year, and rating in variables and print them in a formatted string.

# movie_name = "Hanuman"
# release_year = 2025
# rating = 9.2

# print(f"My favorite movie is {movie_name}, and release {release_year},with ratting of {rating}/10.")



# 3. Take input from the user and check its data type using type().

# user = 52.20

# print(type(user))

# 4. Write a program that accepts two integers and prints their sum, difference, product, and quotient.

# a = 50

# b = 80

# print("Sum:", a + b)
# print("Difference:", a - b)

# print("Product:", a * b)
# print("quotient:", a/b)


# 5. Write a program that takes three numbers and prints the largest one using comparison operators


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


# 6. Create a program to find the remainder when one number is divided by another

# num1 = int(input("Enter the num: "))
# num2 = int(input("Enter the num: "))

# remainder = num1 % num2

# print(f"The remainder {num1} divided by {num2} is {remainder}")


# 7. Write a program to check if a given year is a leap year


# year = int(input("Enter a year: "))

# if (year % 4 == 0) and (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# 8. Create a simple calculator using if-elif-else (add, subtract, multiply, divide).
  

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


# 9.  Write a program to check whether the entered password length is strong (≥8) or weak.


# password = input("Enter password:")

# if len(password) >= 8:
#     print("Strong password")
    
# else:
#     print("Weak password")


# 10. Print a pattern:

for i in range(1, 10):
    for j in range(i):
        print("*", end=' ')
    print()

