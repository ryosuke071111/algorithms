#問題：ながさnの数列を出力する
# ①55555以下の素数
# ②どの異なる5個を選んでも合計は合成数になる
# →合成数にならない条件を抽出してif分当てる
#→素数表にあったらだめ
#→
n=int(input())
NMAX=55555
is_prime = [True]*NMAX
for i in range(2, NMAX):
    if is_prime[i]:
        for j in range(2*i, NMAX, i):
            is_prime[j] = False

prime=[]
for i in range(len(is_prime)):
  if is_prime[i] == True:
    prime.append(i)
    is_prime[i]=False
prime=[i for i in prime if i%5==1]
prime=prime[1:]
ans=prime[:n]
print(*ans)
