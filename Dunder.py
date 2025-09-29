# # 1. Create a class Book with __str__ to display book details.


# class Book:
#     def __init__(self,author, year):
#         self.author = author
#         self.year = year

#     def __str__(self):
#         return f"Book details: , {self.author}, {self.year}"

# b = Book("Pushpendra", 2005)
# print(b)   



# # 2. Implement __len__ for a Playlist class that returns number of songs.


# class Playlist:
#     def __init__(self, song):
#         self.song = song

#     def __len__(self):
#         return len(self.song)

# p = Playlist(["song A", "Song B", "Song C", "song D"])
# print(len(p))  



# # 3. Overload the + operator for a BankAccount class to add balances.


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def __add__(self, other):
#         return {self.balance + other.balance}

#     def __str__(self):
#         return f"Balance:  {self.balance}"

# b1 = BankAccount = 50000
# b2 = BankAccount = 20000
# b = b1 + b2
# print(b)


# # 4. Create a class Student where == compares based on marks.


# class Student:
#     def __init__(self,marks):
#         self.marks = marks

#     def __eq__(self, other):
#         return {self.marks == other.marks}

#     def __str__(self):
#         return f"student marks: {self.marks}"

# st1 = Student("math: 80")
# st2 = Student("science: 90")
# st3 = Student("computer: 85")
# st4 = Student("english: 70")
# print(st1 == st2)


# # 5. Implement a Vector class that supports +, -, and *.


# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, other):
#         return Vector({self.a + other.a, self.b + other.b})

#     def __sub__(self, other):
#         return Vector({self.a - other.a, self.b -other.b})

#     def __mul__(self, other):
#         return Vector({self.a * other.a, self.b * other.b})

#     def __str__(self):
#         return f"value: {self.a}, {self.b}"


# v1 = Vector(10, 20)
# v2 = Vector(5, 10)
# print(v1 * v2)


# 6. Make a class Counter callable using __call__ to increase count.

# class Counter:
#     def __init__(self):
#         self.count = 0

#     def __call__(self):
#         self.count += 1
#         return self.count


# c = Counter()
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())



# # 9. Use __repr__ to return unambiguous details of an object.

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return(f"My name is: {self.name}, age: {self.age} year.")

# p = person("Pushpendra baghel", 23)
# print(p)


# # 10. Combine __str__, __len__, and __add__ in a single class.


# class Employee:
#     def __init__(self, name, income):
#         self.name = name
#         self.income = income
    
#     def __str__(self):
#         return (f"Employee name: {self.name}, income: {self.income} ")

#     def __len__(self):
#         return len({self.name}, {self.income})

#     def __add__(self, other):
#         return (self.name + other.name, self.income + other.income)

#     def __repr__(self):
#         return (f"employee name: {self.name} salary: {self.income}")


# em = Employee("Pushpendra baghel", 30000)
# # em = Employee["pushpa", "raju", "singham"]

# em1 = Employee("Pushpendra baghel", 30000)
# em2 = Employee(" shivam baghel", 20000)

# em3 = em1 + em2
# print(em3)








