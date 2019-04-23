def einfache_funktion(x, **kwargs):
    print('x =', x)
	# die restlichen Argumente sind im Dictionary kwargs
    print('kwargs =', kwargs)   

einfache_funktion(x='Hey', farbe='rot', durchmesser=10)
