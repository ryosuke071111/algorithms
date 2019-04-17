from math import factorial

mod = 10**9+7

w,h = map(int,input().split())

print(factorial(w+h-2)*pow(factorial(w-1),mod-2,mod)*pow(factorial(h-1),mod-2,mod)%mod)

#Aで割りたいときはAのmod-2乗してmodしたものとかけるとそうなる
#今回の場合割りたいものが二つあるから二つで同じことしている
