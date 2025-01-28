class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def pozdrav(self):
        print(f"Ahoj volám sa {self.name} a mám {self.age} rokov")

eugen = Person(name="Eugen", age=36, gender="muz", occupation="Bratislava")
eugen.pozdrav()
patrik = Person(name="Patrik", age=30, gender="muz", occupation="Bratislava")
patrik.pozdrav()

