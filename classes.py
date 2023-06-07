# class Person:
#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location

#     def sayHello(self):
#         print(f'Hello there my name is {self.name} I am {self.age} years old and I live in {self.location}.')


# class Police(Person):
#     def __init__(self, name, age, location, occupation):
#         super().__init__(name, age, location)
#         self.occupation = occupation


# Jayson = Police("Jayson", 18, "Nairobi - Kenya", "Navy seal")
# Jayson.sayHello()
# print(f" I work as a {Jayson.occupation} in the {Jayson.location} army.")


# class Car:
#     def __init__(self, name, year, price):
#         self.name = name
#         self.year = year
#         self.price = price

#     def build__car(self):
#         print(f"This car is called {self.name} made in the year {self.year} and it will cost you {self.price}")


# Urus = Car("Urus", 2022, 170000)

# Urus.build__car()

class city:
    def __init__(self,name,country) -> None:
        self.name=name
        self.country= country

    def name_city(self) -> None:
        print(f"{self.name} is a city located in {self.country}")

Nairobi = city("Nairobi","Kenya")

Nairobi.name_city()