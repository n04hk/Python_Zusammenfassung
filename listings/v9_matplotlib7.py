x = np.logspace(-2, 1, 20)
s = np.exp(-x)

fig, ax = plt.subplots()
ax.loglog(x, s, '.-');
ax.grid(which='both');
