eingabe = '10Fr.'
try:
    x = int(eingabe)
    y = 1/x
except (ValueError, ZeroDivisionError):
    print('Oops! Bitte wiederholen.')
