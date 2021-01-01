def stair(n):

    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return stair(n-3) + stair(n-2) + stair(n-1)


n = int(input())
print(stair(n))
