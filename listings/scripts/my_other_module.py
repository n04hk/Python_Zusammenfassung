class Bank:
    def __init__(self):
        self.__guthaben = 0

    @property
    def guthaben(self):
        print('Das Guthaben wurde abgefragt.')
        return self.__guthaben

    @guthaben.setter
    def guthaben(self, n):
        self.__guthaben = n
        print('Das Guthaben wurde auf {} geaendert.'.format(self.__guthaben))

if __name__ == '__main__':
    b = Bank()
    b.guthaben = 1000
    print(b.guthaben)
	# Konsolen-Ausgabe:
	# Das Guthaben wurde auf 1000 geaendert.
	# Das Guthaben wurde abgefragt.
	# 1000
