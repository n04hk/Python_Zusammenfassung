m = re.search(r'(\d+) ([a-z]+)', '123 hallo welt!')
if m is not None:
    print('groups():', m.groups())  # groups(): ('123', 'hallo')
    print('group(0):', m.group(0))  # group(0): 123 hallo
    print('group(1):', m.group(1))  # group(1): 123
    print('group(2):', m.group(2))  # group(2): hallo

# Mit benannten Gruppen:
m = re.search(r'(?P<zahl>\d+) (?P<wort>\w+)', '123 hallo welt!')
print(m.group('zahl')) # Ausgabe: 123
print(m.group('wort')) # Ausgabe: hallo
m.groupdict()  # als Dictionary
# Ausgabe: {'zahl': '123', 'wort': 'hallo'}
