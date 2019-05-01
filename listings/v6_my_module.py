class MeineKlasse:
    def __init__(self, name):
        self.name = name

    def gruss(self):
        print('Hallo', self.name)

if __name__ == '__main__':
    k = MeineKlasse('Python')
    k.gruss()
	# Ausgabe: # Hallo Python
