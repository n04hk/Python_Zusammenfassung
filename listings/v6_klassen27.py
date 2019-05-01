class Konto:
    def __init__(self, guthaben, iban):
        self.guthaben = guthaben
        self.iban = iban

    def __float__(self):
        return float(self.guthaben)

    def __add__(self, other):
        return self.guthaben + other.guthaben

    def __sub__(self, other):
        return self.guthaben - other.guthaben

k1 = Konto(50, 'CH42 4738 2934 9267 0878 5')
k2 = Konto(23, 'CH27 1036 5802 2994 9234 3')
print('float(k1) =', float(k1)) # float(k1) = 50.0
print('float(k2) =', float(k2)) # float(k2) = 23.0
print('k1 + k2 =', k1 + k2) # k1 + k2 = 73
print('k1 - k2 =', k1 - k2) # k1 - k2 = 27
