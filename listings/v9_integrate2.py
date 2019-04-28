from scipy.integrate import trapz

x = np.array([0, 1, 1.5, 1.8, 2, 3, 4, 5])
y = np.cos(x) + 2

plt.figure()
plt.plot(x, y, 'o-', label='Samples')
plt.ylim(0, 1.1*np.max(y))
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
