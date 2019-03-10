modul = 'Python'    # globale Variable

def anmeldung():
    print(modul)    # Variable existiert bereits ausserhalb der Funktion

anmeldung() # Ausgabe: Python

def wechseln():
    modul = 'C++'   # erstellt eine neue lokale Variable
    print('lokal:', modul)

wechseln()  # Ausgabe: lokal: C++
print('global:', modul) # Ausgabe: global: Python

def wirklich_wechseln():
    global modul    #referenzieren auf die globale Variable
    print('lokal:', modul)

wechseln()  # Ausgabe: lokal: C++
print(global:), modul   # Ausgabe: global: C++
