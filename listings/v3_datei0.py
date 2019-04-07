fr = open('dokument.txt', 'r')  # Datei zum lesen oeffnen
fw = open('dokument.txt', 'w')  # Datei zum schreiben oeffnen

inhalt = fr.read()              # gesamte Datei lesen
inhalt = fr.read(n)             # n Zeichen lesen
zeilen = fr.readlines()         # Liste aller Zeilen

fw.write('hello')               # String schreiben
fw.writelines(['1', '2'])       # Liste von Strings

fr.close()                      # Dateien schliessen
fw.close()