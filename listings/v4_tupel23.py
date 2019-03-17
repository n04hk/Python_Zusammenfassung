from functools import reduce

# (((10 + 20)/2 + 30)/2 + 40)/2
reduce(lambda x, y: (x + y)/2, [10, 20, 30, 40])    # Ausgabe: 31
