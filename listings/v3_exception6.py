try:
  f = open('datei.txt')
except IOError:
    print('Kann Datei nicht oeffnen.')
else: # Wird ausgefuert wenn keine exeptions auftraten
    print('Datei schliessen.') 
    f.close()
print('Ende')
