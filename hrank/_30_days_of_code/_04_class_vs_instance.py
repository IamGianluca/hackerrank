

class Person:

    def __init__(self, initial_age):
        self.age = initial_age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print('Age is not valid, setting age to 0.')
            self._age = 0
        else:
            self._age = value

    def year_passes(self):
        self.age += 1

    def am_i_old(self):
        if self.age < 13:
            print('You are young.')
        elif self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

