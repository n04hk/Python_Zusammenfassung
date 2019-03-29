class MeineKlasse:

    def __init__(self):
        self.pub = 'Ich bin oeffentlich.'
        self._prot = 'Ich bin protected.'
        self.__priv = 'Ich bin privat.'

    def pub_funktion(self):
        print(self.pub)

    def _prot_funktion(self):
        print(self._prot)

    def __priv_funktion(self):
        print(self.__priv)

objekt = MeineKlasse()
