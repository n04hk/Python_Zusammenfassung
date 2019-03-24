m = re.search(r'[a-z]+', '123 hallo welt!')
print(m)
# Ausgabe: <re.Match object; span=(4, 9), match='hallo'>

if m is not None:
    print('group:', m.group())
    print('start:', m.start())
    print('end:', m.end())
    print('span:', m.span())
else:
    print('keine Uebereinstimmung')
# Ausgabe:
# group: hallo
# start: 4
# end: 9
# span: (4, 9)
