import sys
sys.path.append('scripts')
print('\n'.join(sys.path))  # Liste der Suchorte
# Ausgabe: *alle in Frage kommenden Verzeichnisse*

from my_other_module import Bank # Ausgabe:
# Dies ist scripts\my_other_module.py:
# __name__ = my_other_module
b = Bank()
b.guthaben = 500.0 # Ausgabe: Das Guthaben wurde auf 500.0 geaendert.
