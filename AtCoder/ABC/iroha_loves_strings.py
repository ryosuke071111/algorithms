n,l = map(int,input().split())
strings=[input() for i in range(n)]
strings.sort()
print("".join(strings))
