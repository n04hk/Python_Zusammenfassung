arr = np.arange(8)
print(arr) # Ausgabe: array([0, 1, 2, 3, 4, 5, 6, 7])
s = arr[2:5] # array([2, 3, 4])
s[0] = 13 # modifiziert auch arr
print(arr) # Ausgabe: array([0, 1, 13, 3, 4, 5, 6, 7])
