class Fahrzeug:
    def __init__(self, antrieb, **kwargs):
        print('Fahrzeug.__init__(),', 'kwargs =', kwargs)
        super().__init__(**kwargs)
        self.antrieb = antrieb

class Computer:
    def __init__(self, display, **kwargs):
        print('Computer.__init__(),', 'kwargs =', kwargs)
        super().__init__(**kwargs)
        self.display = display

class Tesla(Fahrzeug, Computer):
    def __init__(self, display, dual_motor, **kwargs):
        print('Tesla.__init__()')
        super().__init__(
            antrieb='elektrisch',
            display=display,
            **kwargs
        )
        self.dual_motor = dual_motor


t = Tesla(display='17 Zoll', dual_motor=True) # Ausgabe:
# Tesla.__init__()
# Fahrzeug.__init__(), kwargs = {'display': '17 Zoll'}
# Computer.__init__(), kwargs = {}
t.__dict__ # Ausgabe: {'display': '17 Zoll', 'antrieb': 'elektrisch', 'dual_motor': True}
