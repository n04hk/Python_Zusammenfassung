# Positive, vorausschauende Annahme
re.findall(r'\w+(?=.doc)', 'bericht.doc dokument.doc')  # Nach dem Wort muss ".doc" folgen
# Ausgabe: ['bericht', 'dokument']

# Negative, vorausschauende Annahme
re.findall(r'[A-Za-z]+(?!\d+)\b', 'abc123 cde') # Nach den Wort darf keine Ziffer folgen
# Ausgabe: ['cde']

# Positive, nach hinten schauende Annahme
re.findall(r'(?<=#)\d+', '#10, #25, 66')  # Vor den Ziffern muss ein #-Zeichen sein
# Ausgabe: ['10', '25']

# Negative, nach hinten schauende Annahme
re.findall(r'\b(?<!#)\d+', '#10, #25, 66')  # Vor den Ziffern darf kein #-Zeichen sein:
# Ausgabe: ['66']
