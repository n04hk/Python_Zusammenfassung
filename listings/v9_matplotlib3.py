fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(np.random.randn(10));
ax2.plot(np.random.randn(10));
fig.tight_layout()
