def distanz(x, y, z):
    print('x =', x)
    print('y =', y)
    print('z =', z)
    return (x**2 + y**2 + z**2)**0.5

position = (2, 3, 6)
distanz(*position)  # Tupel entpacken
