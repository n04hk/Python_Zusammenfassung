def counter():
    n = 0
    while True:  # next() setzt wert auf None, send(x) auf x
        wert = yield n
        if wert is not None:
            n = wert
        else:
            n += 1

c = counter()
next(c)			# Ausgabe: 0
c.send(50)	# Ausgabe: 50
next(c)			# Ausgabe: 51
