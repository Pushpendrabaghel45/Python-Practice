                        # Step=1( Create a Car class with attributes: brand, model, and year)
                     

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car : {self.year} {self.brand} {self.model}")

my_car = Car("Toyota", "Corolla", 2020)
# print(my_car.display_info())
my_car.display_info()


                #   Step=2( Add a method start() that prints "Car is starting")
                

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start(self):
#         print(f"Car is starting.....")


#     def display_info(self):
#         print(f"Car : {self.year} {self.brand} {self.model}")


# car1 = Car("Honda", "Civic", 2021)
# car2 = Car("Tata", "Nexon", 2022)
# car3 = Car("Toyota", "Corolla", 2020)
# car1.start()

# # print(car1.display_info())
# # print(car2.display_info())
# # print(car3.display_info())

# car1.display_info()
# car2.display_info()
# car3.display_info()



#                           Step=3(Create 2 different car objects and call the method)


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start(self):
#         print(f" {self.brand} {self.model} is starting.....")

#     def display_info(self):
#         print(f"Car : {self.year} {self.brand} {self.model}")

# # Create two car objects
# car1 = Car("Honda", "Civic", 2021)
# car2 = Car("Tata", "Nexon", 2022)


# #call methods
# car1.start()
# car1.display_info()

# car2.start()
# car2.display_info()


                  #  Step=4( Add another method car_info() that returns brand, model, and year)
  

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start(self):
#         print(f" {self.brand} {self.model} is starting.....")

#     def display_info(self):
#         print(f"Car : {self.year} {self.brand} {self.model}")

#     def car_info(self):
#         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

# # Create two car objects
# car1 = Car("Honda", "Civic", 2021)
# car2 = Car("Tata", "Nexon", 2022)


# #call methods
# print(car1.car_info())
# print(car2.car_info())  
