# class Person:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

#     def introduce(self):
#         print(f"My name is {self.name} and I live in {self.city}.")

# # Creating an object
# p1 = Person("Aamir", "Delhi")

# # Calling method
# p1.introduce()


# class Person:
#     def __init__(self, name, age):
#         self.name = name # store the name inside the object
#         self.age = age  # store the age inside the object

#     def greet(self):
#         print(f"Hello, my name is {self.name} and my age is {self.age}")


# p1 = Person("Aamir", 28)
# p1.greet()

class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        print(f"This Car is a {self.brand} made in {self.year}")

car1 = car("Honda", 2015)
car1.describe()        

