s = re.sub(r'(\d+)/(\d+)/(\d+)', r'\2.\1.\3', '03/20/2019')  # mit Gruppen-Referenzen
print(s) # Ausgabe: 20.03.2019
