def convert8(num):
  ans=0
  for i in range(len(num)):
    ans+=int(num[i])*(8**i)
  return ans


nums={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
num=input()[::-1]
n=""
for i in num:
  n+=str(nums[i])
print(convert8(n))
