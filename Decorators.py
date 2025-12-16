 # 1. Write a decorator that prints "Function is starting..." before and "Function has finished." after any function runs.


# def My_Decorator(function):
#     def wrapper():
#         print("Function is starting....")
#         function()
#         print("Function has finished.")

#     return wrapper

# @My_Decorator
# def say_hello():
#     print("Hello Prem.")


# say_hello()


# # 2. Create a decorator that counts how many times a function is called.

# def count_calls(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         print(f"Call {wrapper.calls}")
#         return func(*args, **kwargs)
#     wrapper.calls = 0
#     return wrapper

# @count_calls
# def call():
#     print("Hello Frameboxx!")
# call()
# call()


# 3. Write a decorator that checks if the user’s age is 18 or above before allowing access to a function.


def age_check(func):
    def wrapper(age, *args, **kwargs):
        if age < 18:
            print(" not elagable to vote for")
            return none
        return func(age, *args, **kwargs)
    return wrapper


@age_check
def decorator(age):
    print("Elagable to vote")
decorator(22)

