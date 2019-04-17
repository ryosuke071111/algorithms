N = int(input())
if N%2:
    N = (N-1)/2
    result = 2*N*(N-1) + 1
else:
    N = N/2
    result = 2*N*(N-1)
print(int(result))
