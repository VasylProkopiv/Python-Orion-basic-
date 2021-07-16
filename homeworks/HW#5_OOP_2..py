class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"return {self.name} and {self.surname} and {self.age}"


vasyl = Human("Vasyl", "Prokopiv", 36)

print(vasyl)