class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def give_message(self):
        print(
            f"Hey my name is {self.name} I am {self.age} years old and I live in {self.location}."
        )


class Police(Person):
    def __init__(self, name, age, location, occupation):
        super().__init__(name, age, location)
        self.occupation = occupation

    def say_occupation(self):
        print(f"Hello my occupation is {self.occupation} .")


name = str(input("What is your name? : "))
age = int(input(f"Hello there {name} what is your age? : "))
location = str(input(f"{name} where do you live? : "))
jayson = Person(name, age, location)
police_man = Police(name, age, location, "Police")
police_man.say_occupation()
jayson.give_message()
