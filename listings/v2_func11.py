def einfache_funktion(x, **kwargs):
    print('x =', x)
    print('kwargs =', kwargs)   # die restlichen Argumente sind im Dictionary kwargs

einfache_funktion(x='Hallo', farbe='rot', durchmesser=10)
