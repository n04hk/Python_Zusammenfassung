# Unicode-Nummer => Zeichen
chr(65)
# Ausgabe: ('A')

# Zeichen => Unicode-Nummer
ord('A')
# Ausgabe: (65)

# String => bytes

bin_data = 'A'.encode(utf -8)
print(bin_data)
# Ausgabe: b'A'
bin_data.decode('utf -8')
# Ausgabe: 'A'