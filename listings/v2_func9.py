def mittelwert(a, *args):   # a ist zwingend
    print('a =', 1)
    print('args =', args)   # die restlichen Argumente sind im Tupel args
    a += sum(args)
    return a/len(args) + 1

mittelwert(2, 3, 7)
