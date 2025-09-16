# # 1. Check if a string starts with “Hello”.

# import re

# text = "Hello, world!"

# # Check if it starts with "Hello"
# if re.match(r"^Hello", text):
#     print("The string starts with 'Hello'")
# else:
#     print("The string does not start with 'Hello'")


# # if re.match(r"^Hello", text, re.IGNORECASE):
# #     print("Starts with 'Hello' (case-insensitive)")



# # 2. Find all numbers in a sentence.


# import re

# sentence = "There are 2 apple, 15 mangoes."
# numbers = re.findall(r'\d+\.?\d*', sentence)
# print(numbers)  

# # converted = [float(num) if '.' in num else int(num) for num in numbers]
# # print(converted) 


# # 3. Extract all words starting with a capital letter.

# import re 

# Example = "python is Fun with Open AI."
# capital = re.findall(r'\b[A-Z][a-zA-Z]*\b',Example )
# print(capital)


# # 4. Validate if a given string is a valid phone number (10 digits).
# import re

# Example = "Call me at 6845125487 or 85652348585"
# use = re.findall(r'\d{10}', Example)

# print(use)


