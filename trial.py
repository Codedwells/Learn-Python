class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def sayHello(self):
        print(f"My name is {self.name} I am {self.age} years. I live in {self.location}")


john = Person("John", 20, "Nairobi")

john.sayHello()
