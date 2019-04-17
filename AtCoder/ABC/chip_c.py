sublN = int(input())
result = 0
for i in range(1,N+1):
    result += ((i**10 - (i-1)**10)*(int(N/i))**10)
result %= 1000000007
print(int(result))
