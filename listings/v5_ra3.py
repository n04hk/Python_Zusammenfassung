m = re.search(r'[a-z]+', '123 hallo welt!')
print(m)
# <re.Match object; span=(4, 9), match='hallo'>

if m is not None:
    print('group:', m.group())  # group: hallo
    print('start:', m.start())  # start: 4
    print('end:', m.end())      # end: 9
    print('span:', m.span())    # span: (4, 9)
