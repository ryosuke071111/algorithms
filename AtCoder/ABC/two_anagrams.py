s=input()
t=input()
s = list("".join(list(s)))
t = list("".join(list(t)))
s=sorted(s)
t=sorted(t,reverse=True)


if t > s:
    print("Yes")
else:
    print("No")
