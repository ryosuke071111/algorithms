n,m,x,y=map(int,input().split())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
z=max(X)+1

print("No War" if x<z <= min(Y) and z<=y else "War")


