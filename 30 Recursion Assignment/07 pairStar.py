def func(s):
    if len(s) == 1:
        return s

    elif s[0] == s[1]:
        return s[0] + "*" + func(s[1:])

    else:
        return s[0] + func(s[1:])


s = input()
print(func(s))
