re.findall(r'\w+$', 'Hallo Welt') # Ausgabe: ['Welt']
re.findall(r'\w+$', 'Punkt A\nPunkt B', flags=re.MULTILINE) # Ausgabe: ['A', 'B']
re.findall(r'\d\Z', '123456') # Ausgabe: ['6']
