x = (1, 2, 3)
y = (7, 8, 9)

def foo(a, b):
	# Objekt veraendern ist nicht erlaubt
	# a.append(4)       
	
	#lokale Variable b referenziert neues Objekt
	b = (10, 11, 12)

foo(x, y)
print('x =', x)  # Ausgabe: x = (1, 2, 3)
print('y =', y)  # Ausgabe: y = (7, 8, 9)
