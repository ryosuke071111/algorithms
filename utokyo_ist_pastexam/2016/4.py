def convert10(num):
  ans=0
  for i in range(len(num)):
    ans+=int(num[i])*(10**i)
  return ans


nums={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"IV":4,"V":5,"I":1}
num=input()
n=0
i=0
while i<len(num):
  if i+1<len(num) and num[i]+num[i+1] in nums:
    n+=nums[num[i]+num[i+1]]
    i+=2
  else:
    n+=nums[num[i]]
    i+=1
print(n)
