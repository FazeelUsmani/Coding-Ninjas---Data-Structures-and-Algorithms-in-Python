# Read input as specified in the question.
# Print output as specified in the question.
def pro(m, n):
    if m == 0 or n == 0:
        return 0
    elif m < n:
        return n + pro(m-1, n)
    else:
        return m + pro(m, n-1)


m = int(input())
n = int(input())
print(pro(m, n))
