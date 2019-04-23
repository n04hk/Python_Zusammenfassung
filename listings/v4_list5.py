fruechte = ['Apfel', 'Erdbeer', 'Clementine', 'Kokosnuss', 'Birne', 'Himbeere']
fruechte_abc = []  # konventionell:
for frucht in fruechte:
    if frucht[0] in 'ABC':
        fruechte_abc.append(frucht)

fruechte_abc = [frucht for frucht in fruechte if frucht[0] in 'ABC']  # mit Listen-Abstraktion: