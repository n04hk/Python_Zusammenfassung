iterator = iter(liste)  # Iterator aus Liste erzeugen
print(type(iterator))  # Ausgabe: <type 'listiterator'>

print('__iter__():', hasattr(iterator, '__iter__'))
print('__next__():', hasattr(iterator, '__next__'))
# Ausgabe:  ('__iter__():', True)
#           ('__next__():', False)

next(iterator)  # Ausgabe: 1
next(iterator)  # Ausgabe: 2
next(iterator)  # Ausgabe: 3 ... bis kein Element drin ist => StopIteration-Exception
