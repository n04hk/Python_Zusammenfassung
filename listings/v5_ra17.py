# Enweder...oder...
for m in re.finditer(r'\d+(V|A)', '230V und 10A bei 23Ohm'):
    print(m.group())
# Ausgabe:
# 230V
# 10A

# Anfang des Strings
re.findall(r'^\w+', 'Hallo Welt') # Ausgabe: ['Hallo']
re.findall(r'^\w+', 'Erste Zeile\nZweite Zeile', flags=re.MULTILINE) # Ausgabe: ['Erste', 'Zweite']
re.findall(r'\A\d', '123456') # Ausgabe: ['1']

# Ende des Strings
re.findall(r'\w+$', 'Hallo Welt') # Ausgabe: ['Welt']
re.findall(r'\w+$', 'Punkt A\nPunkt B', flags=re.MULTILINE) # Ausgabe: ['A', 'B']
re.findall(r'\d\Z', '123456') # Ausgabe: ['6']

# Wortgrenze
re.sub(r'\bschoen\b', 'herrlich', 'Das Wetter ist schoen oder unschoen.')
# Ausgabe: 'Das Wetter ist herrlich oder unschoen.'
