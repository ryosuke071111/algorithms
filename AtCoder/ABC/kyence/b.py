s = input()
n = len(s)

for i in range(n):
    for j in range(i, n):
        tmp = s[:i]+s[j:]
        if tmp == "keyence":
            print("YES")
            quit()

print("NO")
