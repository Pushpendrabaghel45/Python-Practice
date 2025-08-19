# try:
#     a = 10 / 5
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# finally:
#     print("Execution completed.")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Invalid input. Please enter a number.")
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# finally:
#     print("Try block execution done.")



# try:
#     x = int(input("Enter number: "))
#     print("Result:", 10 / x)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("No errors occurred.")
# finally:
#     print("Finished.")


# class BankBalanceError(Exception):
#     def __init__(self, message, balance):
#         self.message = message
#         self.balance = balance

#     def __str__(self):
#         return f"{self.message} (Balance: ₹{self.balance})"

# def withdraw(balance, amount):
#     if amount > balance:
#         raise BankBalanceError("Insufficient Balance", balance)
#     print("Withdrawal Successful")

# try:
#     withdraw(1000, 1500)
# except BankBalanceError as e:
#     print("Transaction failed:", e)



