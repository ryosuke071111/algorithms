A=[int(input()) for i in range(5)]
k=int(input())
for i in range(len(A)):
  for j in range(i+1,len(A)):
    if abs(A[i]-A[j])>k:
      print(':(')
      exit()
print("Yay!")
