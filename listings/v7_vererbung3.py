class Person:
    var = 123

    def func(self):
        print('Person')

class Angestellter(Person):
    pass


a = Angestellter()
print(a.var) # Ausgabe: 123
a.func() # Ausgabe: Person
