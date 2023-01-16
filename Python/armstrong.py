def Armstrong(n):
    listOfIntegersInN = []
    sommeCubique = 0
    while n != 0:
        listOfIntegersInN.append(n%10)
        n = n // 10
    for i in listOfIntegersInN:
        sommeCubique = sommeCubique + i**3
    if n == sommeCubique:
        return True
    elif n != sommeCubique:
        return False
Armstrong(153)
