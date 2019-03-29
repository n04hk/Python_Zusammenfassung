# -*- coding: utf-8 -*-
print('Dies ist {}:\n__name__ = {}'.format(__file__, __name__))

class MeineKlasse:
    def __init__(self, name):
        self.name = name

    def gruss(self):
        print('Hallo', self.name)

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    k = MeineKlasse('Python')
    k.gruss()

# Konsolen-Ausgabe:
# Dies ist C:/Users/Noah/Documents/GitHub/Python_Zusammenfassung/listings/v6_my_module.py:
# __name__ = __main__
# Hallo Python
