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
        self.__priv_func()  # nicht erreichbar, kann in der Subklasse wiederbenutzt werden


sub = SubKlasse() # Ausgabe:
# public Methode
# protected Methode

# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-12-479270c9858a> in <module>
# ----> 1 sub = SubKlasse()

# <ipython-input-11-1794f0b16121> in __init__(self)
#       3         self.pub_func()
#       4         self._prot_func()
# ----> 5         self.__priv_func()  # nicht erreichbar, kann in der Subklasse wiederbenutzt werden

# AttributeError: 'SubKlasse' object has no attribute '_SubKlasse__priv_func'
