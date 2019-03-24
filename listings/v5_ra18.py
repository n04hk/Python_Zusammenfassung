re.findall(r'^\w+', 'Hallo Welt') # Ausgabe: ['Hallo']
re.findall(r'^\w+', 'Erste Zeile\nZweite Zeile', flags=re.MULTILINE) # Ausgabe: ['Erste', 'Zweite']
re.findall(r'\A\d', '123456') # Ausgabe: ['1']
