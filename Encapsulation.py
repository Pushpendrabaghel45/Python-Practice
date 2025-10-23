# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self._city = "Ahamdabad"
#         self.__salary = 25000

# p1 = person("Pushpendra", 23)
# print(p1.name)
# print(p1._city)
# # print(p1__salary)


# 1. Create a class Account with a private attribute __balance. Add getter and setter methods.

# class Account:
#     def __init__(self, __balance):
#         self.__balance = __balance

#     def get__balance(self):
#         return self.__balance

#     def set_balance(self,amount):
#         if amount >= 0:     
#             self.__balance = amount

#         else:
#             print("invalid amount")


# acc = Account(100000)
# print(acc.get__balance())
# acc.set_balance(2000)
# print(acc.get__balance())


# 2.Make a class Car with public (brand), protected (_mileage), and private (__price) attributes. Print them.


# class car:
#     def __init__(self, brand, mileage, price):
#         self.brand = brand
#         self._mileage = mileage
#         self.__price = price

#     def display(self):
#         print(self.brand)
#         print(self._mileage)
#         print(self.__price)

# car = car("Thar", 18, 2000000)

# car.display()


