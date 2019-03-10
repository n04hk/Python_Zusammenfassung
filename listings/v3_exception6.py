try:
  f = open('datei.txt')
except IOError:
    print('Kann Datei nicht oeffnen.')
else:
    print('Datei schliessen.')
    f.close()
print('Ende')
