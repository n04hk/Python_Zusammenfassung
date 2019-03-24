m = re.search(r'(?P<zahl>\d+) (?P<wort>\w+)', '123 hallo welt!')
print(m.group('zahl')) # Ausgabe: 123
print(m.group('wort')) # Ausgabe: hallo
m.groupdict()  # als Dictionary
# Ausgabe: {'zahl': '123', 'wort': 'hallo'}
