eingabe = 5
try:
   if type(eingabe) is list:
       raise SyntaxError
   x = int(eingabe)
   y = 1/x
   if x > 100:
       raise ValueError('Wert ist zu Gross!') #es wird ein Fehler generiert
   f = open('dat.txt')
except (ValueError, IOError) as e: # Mehrere Exception gleich behandeln
    # die Variable e enthaelt die Fehlermeldung
    print('Err: ' + str(e))
except ZeroDivisionError:
    print('Eingabe darf nicht 0 sein!')
else: # Wird ausgefuert wenn kein Fehler auftrat
    print('Alles Okey') 
    f.close()
finally: # Wird immer ausgefuehrt auch wenn das Programm unterbrochen wird
    print('Auf wiedersehen')
print('Prog. laeuft noch')
