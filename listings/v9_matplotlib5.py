x = y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 20, cmap=plt.cm.coolwarm);
cbar = fig.colorbar(CS);
cbar.ax.set_ylabel('C');
