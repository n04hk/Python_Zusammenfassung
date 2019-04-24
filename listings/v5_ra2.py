m = re.match(r'[a-z]+', 'hallo welt!')
print(m)
# <re.Match object; span=(0, 5), match='hallo'>

if m is not None:
    print('group:', m.group())   # group: hallo
    print('start:', m.start())   # start: 0
    print('end:', m.end())       # end: 5
    print('span:', m.span())     # span: (0, 5)
