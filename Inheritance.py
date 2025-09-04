# Practice Inheritance in Python

# Task 1: Single Inheritance

# class Vehicle:
#     def show (self,brand, model ):
#         self.brand = brand
#         self.model = model
        
# class car(Vehicle):
#     def show(self, brand, model, fueltype):
#         super().show(brand, model)
#         self.fueltype = fueltype
        
#     def display_details(self):
#         print(f"Car Brand: {self.brand}")
#         print(f"Car Model: {self.model}")
#         print(f"Fuel Type: {self.fueltype}")

         
# car = car()
# car.show("Mahindra", "Bolero", "Diesel")
# car.display_details()



# Task 2: Multiple Inheritance

# class teacher:
#     def show__teacher(self):
#         print("Teaching...")

# class student(teacher):
#     def show__student(self):
#         print("Learning...")

# class teachingAssistant(teacher, student):
#     def show__teachingAssistant(self):
#         print("Assisting...")

# ta = teachingAssistant()
# ta.show__teacher()
# ta.show__student()
# ta.show__teachingAssistant()



# Task 3: Multilevel Inheritance


# class person:
#     def show__person(self, name):
#         self.name = name

# class employee(person):
#     def show__employee(self, name, salary):
#         super().show__person(name)
#         self.salary = salary

# class manager(employee):
#     def show__manager(self, name, salary, department):
#         super().show__employee(name, salary)
#         self.department = department


#     def display_details(self):
#         print(f"Manager Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Department: {self.department}")

# m = manager()
# m.show__manager("pushpendra", 80000, "HR")
# m.display_details()



#    Task 4: Hierarchical Inheritance
# class shape:
#     def show_shape(self, area):
#         self.area = area
#         print(f"area of the shape: {self.area}")

# class circle(shape):
#     def show_circle(self):
#         print("This is a Circle")

# class rectangle(shape):
#     def show_rectangle(self)
#         print("This is a Rectangle")
    
# circle = circle()
# rectangle = rectangle()

# circle.show_shape()
# circle.show_circle()
# rectangle.show_rectangle()




#   Task 5 using super()

class Animal:
    def sound(self):
        print("Animal make a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dogs...")

d = Dog()
d.sound()
