plt.figure()
ax1 = plt.subplot(2, 1, 1)
ax1.plot(np.random.randn(10));
ax1.set_xlabel('X1')
ax1.set_ylabel('Y1')
ax2 = plt.subplot(2, 1, 2, sharex=ax1)
ax2.plot(np.random.randn(10));
ax2.set_xlabel('X2')
ax2.set_ylabel('Y2')
plt.tight_layout();
