for m in re.finditer(r'[a-z]+', 'hallo welt!'):
    print('---')
    print('group:', m.group())
    print('start:', m.start())
    print('end:', m.end())
    print('span:', m.span())
# Ausgabe:
# ---
# group: hallo
# start: 0
# end: 5
# span: (0, 5)
# ---
# group: welt
# start: 6
# end: 10
# span: (6, 10)
