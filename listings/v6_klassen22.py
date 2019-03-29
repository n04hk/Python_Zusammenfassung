objekt.__dict__ # Ausgabe:
# {'pub': 'Hier macht jeder was er will.',
#  '_prot': 'Ich bin protected.',
#  '_MeineKlasse__priv': 'Ich bin privat.'}

dir(objekt) # Ausgabe:
# ['_MeineKlasse__priv', '_MeineKlasse__priv_funktion', '__class__',
#  '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_prot',
#  '_prot_funktion', 'pub', 'pub_funktion']

objekt._MeineKlasse__priv # Ausgabe: 'Ich bin privat.'
objekt._MeineKlasse__priv_funktion() # Ausgabe: Ich bin privat.
