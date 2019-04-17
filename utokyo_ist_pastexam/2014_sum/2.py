def A1(d,R):
  ans=0
  for x in range(int(R.real)+1):
    for y in range(int(R.imag)+1):
      if 0<=x<=10 and 0<= y <= 10:
        ans+=1
  return ans

def A2(d,R):
  ans=0
  for x in range(int(R.real)+1):
    for y in range(int(R.imag)+1):
      if ((d*x-5)**2)+((d*y-5)**2) <= 25:
        ans+=1
  return ans

d=int(input('please set d:'))
R=complex(5,5)
print(A2(d,R)/A1(d,R)/4)

#-----------------------------------

