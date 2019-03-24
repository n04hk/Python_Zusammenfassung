m = re.search(r'(\d+) ([a-z]+)', '123 hallo welt!')
if m is not None:
    print('groups():', m.groups())
    print('group(0):', m.group(0))
    print('group(1):', m.group(1))
    print('group(2):', m.group(2))
else:
    print('keine Uebereinstimmung')
# Ausgabe:
# groups(): ('123', 'hallo')
# group(0): 123 hallo
# group(1): 123
# group(2): hallo
