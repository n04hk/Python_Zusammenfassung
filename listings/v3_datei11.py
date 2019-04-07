import os
full_path = os.path.abspath('mailaenderli.txt')
print(full_path) # Ausgabe: kompletter Pfad der datei

# Gibt 'true' zurueck wenn full_path eine Datei ist
os.path.isfile(full_path)

# Gibt 'true' zurueck wenn full_path eine Ordner ist
os.path.isdir(full_path)

# Groesse der Datei/Ordner
os.path.getsize(full_path)

# Teilt den Pfad in einen Tupel (Pfad, Dateiname)
os.path.split(full_path)

# Teilt den Pfad in einen Tupel (Pfad, Dateiname, Endung)
os.path.splitext(full_path)

# Macht einen gueltigen Pfad (System abhaengig)
os.path.join('ordner', 'datei.txt')
