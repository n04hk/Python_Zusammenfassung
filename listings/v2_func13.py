modul = 'Python'    # globale Variable

def anmeldung():
	# Variable modul ist Global
	print(modul)    

anmeldung()							# Ausgabe: Python

def wechseln():
	# erstellt eine neue lokale Variable
	modul = 'C++'   
	print('lokal:', modul)

wechseln()							# Ausgabe: lokal: C++
print('global:', modul)	# Ausgabe: global: Python

def wirklich_wechseln():
	# referenzieren auf die globale Variable
	global modul    
	modul = 'C++'
	print('lokal:', modul)

wirklich_wechseln()			# Ausgabe: lokal: C++
print('global:', modul)	# Ausgabe: global: C++
