n=int(input())
nums=sum(list(map(int,("".join(str(n))))))
print('Yes' if n % nums==0 else "No")
