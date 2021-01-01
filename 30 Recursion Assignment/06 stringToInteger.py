
def strConv(s, li):
    # print(li)
    if len(s) == 0:
        return li
    else:
        li.append(ord(s[0]) - 48)
        return strConv(s[1:], li)


s = input()

li = []
li = strConv(s, li)
sum = 0
for i in range(len(li)):
    sum = sum * 10 + li[i]

print(sum, end="")
