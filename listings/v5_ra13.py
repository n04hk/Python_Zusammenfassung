liste = re.findall(r'(\w+)=(\w+)', 'Jahrgang=1930, Name=Hans und Ort=Rappi')
print(liste) # Ausgabe: [('Jahrgang', '1930'), ('Name', 'Hans'), ('Ort', 'Rappi')]
liste = re.findall(r'Ort=(\w+)', 'Jahrgang=1930, Name=Hans und Ort=Rappi')
print(liste) # Ausgabe: ['Rappi']
liste = re.findall(r'(dum)\1', 'dumdum')  # mit Rueckwaertsreferenz der Gruppe
print(liste) # Ausgabe: ['dum']
