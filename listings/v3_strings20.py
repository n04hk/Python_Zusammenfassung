s = '   Dieser String sollte saubere Enden haben.  \n'
print(s)
# Ausgabe:    Dieser String sollte saubere Enden haben.

s.strip()
# Ausgabe: 'Dieser String sollte saubere Enden haben.'

'Ein Satz ohne Satzzeichen am Schluss?'.rstrip('.!?')
# Ausgabe: 'Ein Satz ohne Satzzeichen am Schluss'
