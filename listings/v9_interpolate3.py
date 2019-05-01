# lineare Interpolation
f_lin = interpld(x, y)
# kubische Interpolation
f_cub = interpld(x, y, kind='cubic')
xnew = np.linspace(0, 10, num=101, endpoint=True)
plt.figure()
plt.plot(x, y, 'o', label='Stuetzwerte')
plt.plot(xnew, f_lin(xnew), '-', label='linear')
plt.plot(xnew, f_cub(xnew), '--', label='kubisch')
plt.legend()
plt.show()
