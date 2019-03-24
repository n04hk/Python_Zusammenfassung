liste = re.findall(r'((dum)\2)', 'dumdum')  # (dum) ist jetzt die zweite Gruppe
print(liste) # Ausgabe: [('dumdum', 'dum')]
