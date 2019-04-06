class Angestellter(Person):
    def __init__(self, name, personalnummer):
        # Initialisierungsmethode der Superklasse aufrufen
        super().__init__(name)
        # oder Person.__init__(self, name)
        self.personalnummer = personalnummer
        print('__init__() von Angestellter')
