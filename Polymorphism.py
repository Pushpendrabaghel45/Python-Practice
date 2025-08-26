# # step = 1

# class Calculater:
#     def Add(self, *num):
#         if len(num) == 2:
#            return num[0] + num[1]
#         elif len(num) == 3:
#             return num[0] + num[1] + num[2]

#         else:
#             return "invalid number"


# num1 = Calculater()

# print("Number of sum2:", num1.Add(20,30))

# print("Number of sum3:", num1.Add(10,15,20))

# print("Result:", num1.Add(0))




# step = 2

# class vehicle:
#     def inti (self):
#         print("this is a vehicle")

# class car(vehicle):
#     def inti (self):
#         print("this ia a car")

# class bike(vehicle):
#     def inti (self):
#         print("this is a bike")


# v = vehicle()


# v.inti()
# v.inti()
# v.inti()



# # step = 3

class Complexnumber:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

c1 = Complexnumber(50)
c2 = Complexnumber(60)

print(c1 + c2)
    

# class Student:
#     def __init__(self, marks):
#         self.marks = marks
    
#     def __add__(self, other):
#         return self.marks + other.marks

# s1 = Student(80)
# s2 = Student(90)
# print(s1 + s2)  # 170
