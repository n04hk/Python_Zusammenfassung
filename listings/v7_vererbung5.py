class Person:
    def func(self):
        print('Person')

class Angestellter(Person):
    def func(self):
        super().func()
        print('Angestellter')


a = Angestellter()
a.func() # Ausgabe:
# Person
# Angestellter
