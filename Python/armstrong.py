def Armstrong(nbr):
    sommeCubique = 0
    tmp = nbr
    while tmp > 0:
        d = tmp % 10
        sommeCubique += d ** 3
        tmp //= 10
    if nbr == sommeCubique:
        return True
    else:
        return False

a = []
for x in range(10000):
    if Armstrong(x):
        a.append(x)

print(a)

