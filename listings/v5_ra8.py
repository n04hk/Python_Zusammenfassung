s = re.sub(r'\d+', '<Zahl>', '3 Stuecke kosten 250 Franken.', count=1)
print(s)  # Ausgabe: <Zahl> Stuecke kosten 250 Franken.
