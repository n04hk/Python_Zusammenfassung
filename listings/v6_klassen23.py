class Bank:
    def __init__(self):
        self.__guthaben = 0

    def get_guthaben(self):
        print('Das Guthaben wurde abgefragt.')
        return self.__guthaben

    def set_guthaben(self, n):
        self.__guthaben = n
        print('Neues Guthaben: {}.'.format(self.__guthaben))

k = Bank()
k.set_guthaben(1000000) # Ausgabe: Neues Guthaben 1000000.
print(k.get_guthaben()) # Ausgabe: Das Guthaben wurde abgefragt.
# Ausgabe: 1000000
