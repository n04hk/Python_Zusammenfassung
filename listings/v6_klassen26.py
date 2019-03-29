class Konto:
    def __init__(self, guthaben, iban):
        self.guthaben = guthaben
        self.iban = iban

    def __str__(self):
        return 'IBAN: {}\nGuthaben: {}'.format(self.iban, self.guthaben)

k = Konto(50, 'CH42 4738 2934 9267 0878 5')
print(k) # Ausgabe:
# IBAN: CH42 4738 2934 9267 0878 5
# Guthaben: 50
