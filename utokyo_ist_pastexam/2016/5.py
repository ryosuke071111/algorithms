dic={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"IV":4,"V":5,"I":1}
dic={v:i for i,v in dic.items()}
nums=sorted(dic,reverse=True)

def convertR(num):
  ans=""
  i=0
  while num>0:
    while num>=nums[i]:
      num-=nums[i]
      ans+=dic[nums[i]]
    i+=1
  return ans

n=int(input())
print(convertR(n))
