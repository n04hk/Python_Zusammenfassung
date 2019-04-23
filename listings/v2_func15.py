x = [1, 2, 3]
y = [7, 8, 9]

def foo(a, b):
	# Objekt veraendern
	a.append(4)
	# lokale Variable b referenziert neues Objekt
	b = [10, 11, 12]

foo(x, y)
print('x =', x)  # Ausgabe: x = [1, 2, 3, 4]
print('y =', y)  # Ausgabe: y = [7, 8, 9]
