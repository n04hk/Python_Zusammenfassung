import os
full_path = os.path.abspath('mailaenderli.txt')
print(full_path) # Ausgabe: kompletter Pfad der datei

os.path.isfile(full_path)  # Return 'true' wenn full_path eine Datei ist
os.path.isdir(full_path)  # Return 'true' wenn full_path eine Ordner ist
os.path.getsize(full_path)  # Groesse der Datei/Ordner
os.path.split(full_path)  # Teilt den Pfad in einen Tupel (Pfad, Dateiname)
os.path.splitext(full_path)  # Pfad in einen Tupel (Pfad, Dateiname, Endung)
os.path.join('ordner', 'datei.txt')  # Macht einen gueltigen Pfad (System abhaengig)
