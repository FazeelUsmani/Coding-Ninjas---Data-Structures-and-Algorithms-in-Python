def zeroes(n, cnt):

    if n == 0:
        return cnt

    elif n % 10 == 0:
        return zeroes(n//10, cnt+1)

    else:
        return zeroes(n//10, cnt)


n = int(input())
print(zeroes(n, 0))
