def func(m):
    return '(' + m.group() + ')'

s = re.sub(r'\d+', func, '3 Stuecke kosten 250 Franken.')
print(s)
# Ausgabe: (3) Stuecke kosten (250) Franken.
