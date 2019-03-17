liste = [2, 5, 3, 4, 1]
sortiert = sorted(liste, reverse=True)
print('Liste:', liste)          # Ausgabe: ('Liste:', [2, 5, 3, 4, 1])
print('sortiert:', sortiert)    # Ausgabe: ('sortiert:', [5, 4, 3, 2, 1])

liste.sort(reverse=True)
liste                           # Ausgabe: [5, 4, 3, 2, 1]
