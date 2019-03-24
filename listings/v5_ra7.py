s = re.sub(r'\d+', '<Zahl>', '3 Stuecke kosten 250 Franken.')
print(s)
# Ausgabe: <Zahl> Stuecke kosten <Zahl> Franken.
