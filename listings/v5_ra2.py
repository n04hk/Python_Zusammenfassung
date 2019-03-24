m = re.match(r'[a-z]+', 'hallo welt!')
print(m)
# Ausgabe: <re.Match object; span=(0, 5), match='hallo'>

if m is not None:
    print('group:', m.group())
    print('start:', m.start())
    print('end:', m.end())
    print('span:', m.span())
else:
    print('keine Uebereinstimmung')
# Ausgabe:
# group: hallo
# start: 0
# end: 5
# span: (0, 5)
