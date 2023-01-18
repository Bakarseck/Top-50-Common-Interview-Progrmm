def Armstrong(nbr):
    sommeCubique = 0
    tmp = nbr
    while tmp > 0:
        d = tmp % 10
        sommeCubique += d ** 3
        tmp //= 10
    if nbr == sommeCubique:
        print(nbr,"est un nombre Armstrong")
    else:
        print(nbr,"n'est pas un nombre Armstrong")
Armstrong(153)
