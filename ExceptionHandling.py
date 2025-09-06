

# 1. Create a custom exception TooYoungError. Raise it if age entered is less than 18.

# class TooYoungError(Exception):
#     " exception when raise is less than 18."

#     pass

# def check_age(age):
#     try:
#         if age < 18:
#             raise TooYoungError(f"Age {age} is age less than  18.")

#         print(f"Age {age} is valid.")

#     except TooYoungError as e:
#         print(f"Error: {e}")

# check_age(18)
# check_age(15)


# # 2. Write a BankAccount class where withdrawal raises InsufficientFundsError if balance is low.

# class BankAccount(Exception):
#     def __init__(self, balance):
#         self.balance = balance

#     def withdrawal(self, amount):
#         if amount > self.balance:
#             raise InsufficientFundsError
#         self.balance -= amount
#         return self.balance
# # print(f"Withdrawal successful. Remaining balance: {self.balance}")

# acc = BankAccount(5000)
# acc.withdrawal(2000)
# print(acc)


# # 3. Make a PasswordValidator class. Raise a WeakPasswordError if password is too short.



# # Custom Exception
# class WeakPasswordError(Exception):
#     """Raised when the password is too short."""
#     pass

# # Password Validator Class
# class PasswordValidator:
#     def __init__(self, min_length=8):
#         self.min_length = min_length

#     def validate(self, password):
#         if len(password) < self.min_length:
#             raise WeakPasswordError(f"Password too short. Must be at least {self.min_length} characters.")
#         print("Password is strong.")

# # Example usage
# validator = PasswordValidator()

# try:
#     validator.validate("abc")  # Too short
# except WeakPasswordError as e:
#     print(f"Validation Error: {e}")





# # 4. Create a program that raises an exception if a number is divided by zero (custom error, not ZeroDivisionError).


# class DivisionByZeroError(Exception):
#     """Custom exception for division by zero."""
#     pass

# def safe_divide(a, b):
#     if b == 0:
#         raise DivisionByZeroError("can't divid by zero.")

#     return a / b 

# try:
#     result = safe_divide(100, 18)
#     print(f"Result: {result}")
    
# except DivisionByZeroError as e:
#     print(f"Math error: {e}")


    
# 5. Design a Student class where adding marks raises an exception if marks > 100


class MarksError(Exception):
    """Raise when marks are  greater than."""
    pass

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        if mark > 100:

            raise MarksError(f"mark {mark} is invalid.")

        self.marks.append(mark)
    def average(self):
        return sum(self.marks) / len(self.marks) if self. marks else 0


Student = Student("Pushpendra")

try:
    Student.add_mark(95)
    Student.add_mark(55)

except MarksError as e:
    print(f"marks error: {e}")

