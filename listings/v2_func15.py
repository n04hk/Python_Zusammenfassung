x = [1, 2, 3]
y = [7, 8, 9]

def foo(a, b):
    a.append(4)         # Objekt veraendern
    b = [10, 11, 12]    # lokale Variable b referenziert neues Objekt

foo(x, y)
print('x =', x)
print('y =', y)
