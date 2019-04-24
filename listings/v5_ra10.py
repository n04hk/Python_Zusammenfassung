resultat = re.subn(r'\d+', '<Zahl>', '3 Stuecke kosten 250 Franken.')
print(resultat)  # Ausgabe: ('<Zahl> Stuecke kosten <Zahl> Franken.', 2)
