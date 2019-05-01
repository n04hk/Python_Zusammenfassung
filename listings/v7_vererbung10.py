class SuperKlasse:
    def __init__(self):
        self.pub = 'public Variable'
        self._prot = 'protected Variable'
        self.__priv = 'private Variable'

    def pub_func(self):
        print('public Methode')

    def _prot_func(self):
        print('protected Methode')

    def __priv_func(self):
        print('private Methode')

class SubKlasse(SuperKlasse):
    def __init__(self):
        self.pub_func()
        self._prot_func()
		# nicht erreichbar, kann in der Subklasse wiederbenutzt werden
        self.__priv_func()  

sub = SubKlasse() # Ausgabe:
# public Methode
# protected Methode
# AttributeError...
