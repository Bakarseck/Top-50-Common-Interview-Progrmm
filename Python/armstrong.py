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

    # listOfIntegersInN = []
    # sommeCubique = 0
    # while n != 0:
    #     listOfIntegersInN.append(n%10)
    #     n = n // 10
    # for i in listOfIntegersInN:
    #     sommeCubique = sommeCubique + i**3
    # if n == sommeCubique:
    #     return True
    # elif n != sommeCubique:
    #     return False
Armstrong(153)
