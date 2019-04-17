a,b,c = map(int,input().split())

# a = a%b

for i in range(1, b+1):
  if  a*i % b== c:
    print('YES')
    exit()

print('NO')

#「無限個のAの倍数の総和を選んで良いbで割った結果がcになる問題」
#A*i%bの数がb個からなる集合になる。
