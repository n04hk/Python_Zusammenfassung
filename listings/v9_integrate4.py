from scipy.integrate import quad

def func(x):
    return np.sin(x)**2

# Integration mit Gauss-Quadratur
y, abserr = quad(func, a=0, b=np.pi)
print('y =', y, '; err=', abserr) # Ausgabe:
# y = 1.5707963267948966 ; err= 1.743934249004316e-14
# Analytische Loesung
print('y =', np.pi/2) # Ausgabe:
# y = 1.5707963267948966
