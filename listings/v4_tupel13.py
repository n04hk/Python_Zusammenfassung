liste = ['a', 'b', 'c', 'd', 'e', 'f']

element = liste.pop()  # letztes Element rechts
print(element)  # Ausgabe: f
liste           # Ausgabe: ['a', 'b', 'c', 'd', 'e']

element = liste.pop(0)  # mit Index
print(element)  # Ausgabe: a
liste           # Ausgabe: ['b', 'c', 'd', 'e']

liste.remove('c')  # mit einem bestimmten Wert
liste           # Ausgabe: ['b', 'd', 'e']
