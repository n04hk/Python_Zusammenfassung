spannung = 12.56
strom = 0.5
'U = {}, I = {}'.format(spannung , strom)
# Ausgabe: 'U = 12.56, I = 0.5'

# Mit Index
# ------------------------------------
'U = {0}, I = {1}'.format(spannung , strom)
# Ausgabe: 'U = 12.56, I = 0.5'

# Mit Index und Format:
# ------------------------------------
'U = {0:.2f}, U = {0:.f}'.format(spannung)
# Ausgabe: 'U = 12.56, U = 12.560000'

# Links-/rechtsbuendig oder zentriert:
# ------------------------------------
'{:>8.2f}'.format(sapnnung)
# Ausgabe: ' 12.56'
'{:<8.2f}'.format(spannung)
# Ausgabe: '12.56 '
'{:^8.2f}'.format(spannung)
# Ausgabe: ' 12.56 '

# Mit Schluesselwortparameter:
# ------------------------------------
'U = {u}, I = {i}'.format(u=spannung , i=strom)
# Ausgabe: 'U = 12.56, I = 0.5'

# Mit Dictionary
# ------------------------------------
messung = {'spannung': 24, 'strom': 2.5}
'U = {spannung}, I = {strom}'.format(**messung)
# Ausgabe: 'U = 24, I = 2.5'
