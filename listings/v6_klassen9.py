class MeineKlasse:
    '''Beschreibung der Klasse.'''
    speed_of_light = 299792458

    def __init__(self, name):
        '''Diese Methode initialisiert die Variablen.'''
        self.name = name
        print(self.name, 'wurde erstellt.')

    def __del__(self):
        '''Diese Methode raeumt alles auf bevor es zerstoert wird.'''
        print(self.name, 'wurde zerstoert.')

    def hallo(self):
        '''Sagt Hallo.'''
        print('Hallo', self.name)
