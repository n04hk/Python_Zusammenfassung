eingabe = '10Fr.'
try:
    x = int(eingabe)
    y = 1/x
except ValueError as e:
    print('Oops! ' + str(e))
except ZeroDivisionError as e:
    print('Oops! ' + str(e))
