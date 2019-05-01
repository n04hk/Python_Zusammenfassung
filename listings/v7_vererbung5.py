class Person:
    def func(self):
        print('Person')

class Angestellter(Person): # Fuer die Vererbung: Superklasse in runden Klammern angeben
    def func(self): # Methoden werden ueberschrieben, falls sie gleich heissen:
        super().func() # Zugriff auf die Superklasse mit super()
        print('Angestellter')

a = Angestellter()
a.func() # Ausgabe: Person\nAngestellter
