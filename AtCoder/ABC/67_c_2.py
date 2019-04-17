n=int(input())
A=list(map(int,input().split()))
sumA=sum(A)
T=[0]*n
for i in range(1,n):
  T[i]=T[i-1]+A[i-1]
print(min(abs(sumA-2*T[i]) for i in range(1,n)))


"""
問題にさしあたったときの思考過程
・スライスで差が最小取れば簡単そうだな
・だけど10^5だからO^2はTLEするな
・どうやったらその最小を少ない計算量で取れるのだろう→実装方法が思い浮かばない

正解
・累積和を事前にとっておいて全体の総数から、その地点での累積和を引く
・i枚目までの総和：x_i、残りの総和：y_i=X-xi_i => |y_i-x_i|=|X-2*x_i|
・
"""
