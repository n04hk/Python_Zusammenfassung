class Person:
    def func(self):
        print('Person')

class Angestellter(Person):
    def func(self):
        print('Angestellter')


a = Angestellter()
a.func() # Ausgabe: Angestellter
