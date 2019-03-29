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

help(MeineKlasse)
# Ausgabe:
# Help on class MeineKlasse in module __main__:
#
# class MeineKlasse(builtins.object)
#  |  MeineKlasse(name)
#  |
#  |  Beschreibung der Klasse.
#  |
#  |  Methods defined here:
#  |
#  |  __del__(self)
#  |      Diese Methode raeumt alles auf bevor es zerstoert wird.
#  |
#  |  __init__(self, name)
#  |      Diese Methode initialisiert die Variablen.
#  |
#  |  hallo(self)
#  |      Sagt Hallo.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  speed_of_light = 299792458
