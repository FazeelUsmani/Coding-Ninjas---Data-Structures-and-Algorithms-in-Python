def geometricSum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2, n)) + geometricSum(n - 1)


n = int(input())
result = geometricSum(n)
print('%.5f' % result)
