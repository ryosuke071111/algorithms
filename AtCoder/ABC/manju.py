a,b,c = map(int,input().split())
num_a, amari = divmod(c,min(a,b))
num_b = amari // b

print(num_a+num_b)
