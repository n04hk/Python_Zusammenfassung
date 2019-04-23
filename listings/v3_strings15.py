'Python ist eine      Schlange.'.split()
# Ausgabe: ['Python', 'ist', 'eine', 'Schlange.']

csv = '1;2000;30.3;44;505'
csv.split(';')
# Ausgabe: ['1', '2000', '30.3', '44', '505']

# max. zwei Trennungen von links her
csv.split(';', maxsplit=2)
# Ausgabe: ['1', '2000', '30.3;44;505']

# max. zwei Trennungen von rechts her
csv.rsplit(';', maxsplit=2)
# Ausgabe: ['1;2000;30.3', '44', '505']

'1;2;;;;3;4'.split(';')
# Ausgabe: ['1', '2', '', '', '', '3', '4']
