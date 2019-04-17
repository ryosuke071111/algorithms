n=int(input())
A=list(map(int,input().split()))
A=list(map(lambda x:x//400 if x<3200 else 8,A))
n_red=A.count(8)
red_exist=1 if n_red else 0
n_min=len(set(A)) if not red_exist else len(set(A))-1
print(1 if not n_min else n_min,n_min+n_red)
