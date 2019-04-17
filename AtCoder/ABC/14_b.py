# n,x=map(int,input().split())
# A=list(map(int,input().split()))
# ans=0
# x=str(bin(x))[2:]
# x=x[::-1]
# for i in range(len(x)):
#   if x[i]=="1":
#     ans+=A[i]
# print(ans)




#ビット演算
n,x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    # Xをiビット右に動かした時、1桁目が1かどうか(1 & 1 == 1にできるか)
    if x >> i & 1:
        ans += A[i]
print(ans)
