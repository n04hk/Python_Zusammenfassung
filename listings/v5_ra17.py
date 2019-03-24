for m in re.finditer(r'\d+(V|A)', '230V und 10A bei 23Ohm'):
    print(m.group())
# Ausgabe:
# 230V
# 10A
