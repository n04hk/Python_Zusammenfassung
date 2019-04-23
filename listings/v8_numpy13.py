import numpy as np
import matplotlib.pyplot as plt

t = np.arange(100)/100
s1 = np.sin(2*np.pi*t)
s2 = s1 + np.random.randn(*s1.shape)/4

plt.figure()
plt.plot(t, s1, '.-', label='Simulation')
plt.plot(t, s2, '.-', label='Messung')
plt.xlabel('Zeit (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('diagramm.pdf')
