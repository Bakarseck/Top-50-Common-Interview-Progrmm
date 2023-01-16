def isIPalindrom(n):
    listOfIntegersInN = []
    while n != 0:
        listOfIntegersInN.append(int(n%10))
        n = n//10
    if listOfIntegersInN == listOfIntegersInN[::-1]:
        return True
    else:
        return False