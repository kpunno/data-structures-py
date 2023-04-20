class Person:
    name = ""
    nickname = ""

    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)

class Guy(Person):
    gender = "male"
    def display(self):
        print(self.name, "is a", self.gender)

class Girl(Person):
    gender = "female"
    def display(self):
        print(self.name, "is a", self.gender)

person = Person("buddy")
guy = Guy("Jimmy")
girl = Girl("jammy")

person.display()
guy.display()
girl.display()
