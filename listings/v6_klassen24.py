class Bank:
    def __init__(self):
        self.__guthaben = 0

    def __get_guthaben(self):
        print('Das Guthaben wurde abgefragt.')
        return self.__guthaben

    def __set_guthaben(self, n):
        self.__guthaben = n
        print('Neues Guthaben: {}.'.format(self.__guthaben))

    guthaben = property(__get_guthaben, __set_guthaben)

k = Bank()
k.guthaben = 1000000 # Ausgabe: Neues Guthaben 1000000.
print(k.guthaben) # Ausgabe: Das Guthaben wurde abgefragt.
# Ausgabe: 1000000
