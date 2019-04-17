def A1(d,R):
  return (R.real//d+1)*(R.imag//d+1)

R=complex(10,10)
d=int(input('please set d'))
print(A1(d,R))


