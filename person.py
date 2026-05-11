class Person:
    def __init__(self, first_name, middle_name, last_name, year_of_birth):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def full_name(self):
        print(f"{self.first_name} {self.last_name}")

    def initials(self):
        print(f"{self.first_name[0]}.{self.last_name[0]}.")


person = Person("John", "Michael", "Doe", 1990)
person.full_name()
person.initials()
