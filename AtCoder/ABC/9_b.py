n=int(input())
print(sorted(list(set([int(input()) for i in range(n)])),reverse=True)[1])


