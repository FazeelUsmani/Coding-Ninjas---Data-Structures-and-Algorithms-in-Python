def sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum(n//10)


n = int(input())
print(sum(n))
