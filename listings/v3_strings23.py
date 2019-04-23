spannung = 12.56
strom = 0.5
'U = {}, I = {}'.format(spannung , strom)
# Ausgabe: 'U = 12.56, I = 0.5'

'U = {0}, I = {1}'.format(spannung , strom)  # Mit Index
# Ausgabe: 'U = 12.56, I = 0.5'

'U = {0:.2f}, U = {0:.f}'.format(spannung)  # Mit Index und Format:
# Ausgabe: 'U = 12.56, U = 12.560000'

'{:>8.2f}'.format(sapnnung)  # Rechtsbuendig
# Ausgabe: ' 12.56'
'{:<8.2f}'.format(spannung)  # Linksbuendig
# Ausgabe: '12.56 '
'{:^8.2f}'.format(spannung)  # Zentriert
# Ausgabe: ' 12.56 '

'U = {u}, I = {i}'.format(u=spannung , i=strom)  # Mit Schluesselwortparameter:
# Ausgabe: 'U = 12.56, I = 0.5'

messung = {'spannung': 24, 'strom': 2.5} # Mit Dictionary
'U = {spannung}, I = {strom}'.format(**messung)
# Ausgabe: 'U = 24, I = 2.5'