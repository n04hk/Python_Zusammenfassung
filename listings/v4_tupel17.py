liste = ['laenger', 'lang', 'am laengsten']
sorted(liste, key=len)
# ['lang', 'laenger', 'am laengsten']

# nur [1]-tes Element (stabile Sortierung)
liste = [('a', 3), ('a', 2), ('c', 1), ('b', 1)]
from operator import itemgetter
sorted(liste, key=itemgetter(1))
# [('c', 1), ('b', 1), ('a', 2), ('a', 3)]
sorted(liste, key=lambda x: x[1])
# [('c', 1), ('b', 1), ('a', 2), ('a', 3)]

# Nach 1. Element, dann nach dem 2. sortiern
sorted(liste)  
# [('a', 2), ('a', 3), ('b', 1), ('c', 1)]
